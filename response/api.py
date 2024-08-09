from fastapi import FastAPI,HTTPException
from fastapi.responses import FileResponse 
import os
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import json
app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],  
)

script_directory = os.path.dirname(os.path.abspath(__file__))
json_file_path = os.path.join(script_directory, "omr_data.json")
# Serve the JSON file at a specific route


class Coordinate(BaseModel):
    page_no:int
    x: int
    y: int  
    r:int
    question_no: int = None  # Default to None if not provided
    option: str = ""  # Default to empty string if not provided

@app.get("/json-file")
def serve_json_file():
    if os.path.exists(json_file_path):
        return FileResponse(json_file_path, media_type='application/json')
    else:
        return {"error": "File not found"}
    



@app.post("/json-file")
def update_json_file(coordinates: list[Coordinate]):


    if not os.path.exists(json_file_path):  # Check if the file exists
        raise HTTPException(status_code=404, detail="File not found")
    

    # Read existing content
    with open(json_file_path, 'r') as file:
        content = json.load(file)
    for coord in coordinates:
        coord_dict = coord.dict()
        page_no=coord_dict.get("page_no")
    # Initialize page entry if not present
    if str(page_no) not in content:
        content[str(page_no)] = {"coordinates": []}
    res={}

    # Add new coordinates
    for coord in coordinates:
        coord_dict = coord.dict()
        x=coord_dict.get("x")
        y=coord_dict.get("y")
        r=coord_dict.get("r")
        ques= coord_dict.get("question_no", None)
        opt= coord_dict.get("option", None) 
        res={"x":x,"y":y,"r":r,"question_no":ques,"option":opt}
        content[str(page_no)]["coordinates"].append(res)

    # Write updated content back to file
    with open(json_file_path, 'w') as file:
        json.dump(content, file, indent=4)

    return {"message": "Data updated successfully"}  

