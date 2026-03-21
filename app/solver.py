from pydantic import BaseModel
from typing import List, Dict
from app.ingestion import CargoTask

#1. Define agents (Robots/Trucks)
class Agent(BaseModel):
    agent_id: str
    current_zone: str
    capacity_kg: float

#2. MDP reward function
def calculate_reward(cargo: CargoTask, agent: Agent) -> float:
   
    if cargo.weight_kg > agent.capacity_kg:
        return -9999.0
    
    reward = 0.0

    reward += (cargo.priority*10) # High priority = high reward

    # Negative reward if agent is in different zone
    if agent.current_zone != cargo.destination_zone:
        reward -= 15.0
    else:
        reward += 5.0       # +5 reward for being in right zone
 
    return reward

#3. The dispatch algorithm(Policy)
def optimize_dispatch(cargo_batch: List[CargoTask], agents: List[Agent]) -> Dict[str, List[dict]]:
    
    assignments = {agent.agent_id: [] for agent in agents}
    unassigned = []

    for cargo in cargo_batch:
        best_agent = None
        max_reward = -float('inf')

        #check every agent to see who gets the highest score for this cargo box
        for agent in agents:
            reward = calculate_reward(cargo, agent)

            if reward > max_reward and reward > -1000:
                max_reward = reward 
                best_agent = agent

        
        #assign box to winner
        if best_agent:
            best_agent.capacity_kg -= cargo.weight_kg
            assignments[best_agent.agent_id].append({
                "task_id": cargo.task_id,
                "zone": cargo.destination_zone,
                "reward_score": max_reward
            })
        else:
            unassigned.append(cargo.task_id)
    
    return{"assignments": assignments, "unassigned_tasks": unassigned} 