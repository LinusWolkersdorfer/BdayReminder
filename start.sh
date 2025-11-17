#!/bin/bash

cd backend
if [ ! -d "venv" ]; then
    echo "Erstelle virtuelle Umgebung..."
    python -m venv venv
fi
source venv/Scripts/activate
if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
else
    echo "Keine requirements.txt gefunden. Bitte erstelle eine."
fi
#python main.py &
uvicorn main:app --reload &

cd ../svelte
npm install
npm run dev
