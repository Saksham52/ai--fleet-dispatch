from fastapi import FastAPI
from app.ingestion import generate_incoming_cargo
from app.solver import Agent, optimize_dispatch 
from app.reporter import generate_manager_report

#1. Creating the FastAPI
app = FastAPI(
    title= "Fleet Dispatch API",
    description = "An API to optimize multi-agent cargo dispatching.",
    version = "1.0.0"
)
#2. Define Homepage
@app.get("/")
def read_root():
    """This just proves the server is awake."""
    return {"message": "Welcome to Fleet Dispatch API. The server is running!"}

#3. Define the Cargo Endpoint
@app.get("/dispatch")
def get_optimized_dispatch(batch_size: int= 5):

    live_cargo = generate_incoming_cargo(num_tasks=batch_size)

    fleet = [
        Agent(agent_id= "Robot_Alpha", current_zone="Zone_A", capacity_kg = 200.0),
        Agent(agent_id= "Robot_Beta", current_zone="Zone_C", capacity_kg = 150.0),
        Agent(agent_id= "Robot_Gamma", current_zone="Zone_D", capacity_kg = 100.0)
    ]


    dispatch_plan = optimize_dispatch(live_cargo, fleet)

    report = generate_manager_report(dispatch_plan)

    return{"status": "success",
           "total_cargo": len(live_cargo),
           "manager_report": report["manager_summary"],
           "dispatch_plan": dispatch_plan,
           "prompt_debug": report["llm_prompt_generated"]
           }


