# Copyright 2023 undefined
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from fastapi import FastAPI, HTTPException
import zhipuai

app = FastAPI()

# 设置全局的Zhipuai API密钥
zhipuai.api_key = "6d1e089b49d9a1fc9f251240af39d2ff.sEjOi7HBGjQML5pf"

@app.post("/chat/")
async def chat_with_model(chat_data: dict):
    try:
        response = zhipuai.model_api.sse_invoke(**chat_data)
        chat_result = []
        
        for event in response.events():
            if event.event == "add":
                chat_result.append(event.data)
            elif event.event == "error" or event.event == "interrupted":
                chat_result.append(event.data)
            elif event.event == "finish":
                chat_result.append(event.data)
        
        return {"chat_result": chat_result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/embedding/")
async def text_embedding(text_data: dict):
    try:
        response = zhipuai.model_api.invoke(**text_data)
        data = response.get("data", {})
        embedding = data.get("embedding", [])
        
        return {"embedding": embedding}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
