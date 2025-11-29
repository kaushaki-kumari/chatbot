## Inno AI Assistant - flask + MongoDB Atlas + Chroma + Claude

A lightweight and modular AI Assistant built using Flask, MongoDB Atlas, ChromaDB, Sentence Transformers, and Anthropic Claude.
this allows users to:
✔️ Paste text into a textarea
✔️ Save it to your MongoDB Cloud database
✔️ View/Edit/Delete saved entries in a clean table
✔️ Ask questions in the AI chat
✔️ AI responds strictly from your saved MongoDB data

## 🚀 Features

1. 📝 Data Entry & Storage
   ✔️ Textarea to paste any content
   ✔️ Save button → stores data in MongoDB Atlas
   ✔️ Cancel button → clears input
   ✔️ Auto-refresh data table

2. 📊 Data Management Table
   ✔️ Displays all saved entries
   ✔️ Edit + Update
   ✔️ Delete entry
   ✔️ Scrollable table UI

3. 🧠 AI Assistant
   ✔️ Reads all saved MongoDB data
   ✔️ Converts them into text chunks
   ✔️ Embeds chunks into ChromaDB
   ✔️ Finds best matching chunks
   ✔️ Claude answers strictly using your saved data

4. 🌐 UI & Frontend
   ✔️ Floating chat widget
   ✔️ Editable table
   ✔️ Responsive layout
   ✔️ Clean CSS

5. 🏗️ Backend Architecture
   ✔️ Flask Blueprints (chat_bp, doc_bp)
   ✔️ Separate services for DB, embeddings, chunking
   ✔️ MongoDB Atlas cloud storage
   ✔️ Auto-reloading DB contents

## 🔧 Setup Instructions

1️⃣ Create Virtual Environment
python -m venv venv
source venv/bin/activate # macOS / Linux
venv\Scripts\activate # Windows

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Environment Variables
🔐 Create a .env file:-
MONGO_URI=mongodb+srv://<username>:<password>@<cluster-url>/
ANTHROPIC_API_KEY=your_api_key_here

4️⃣ Run the App
python app.py

## 🧠 How It Works

1. Save Text to DB
   ✔️ User enters text in textarea
   ✔️ Clicks Save
   ✔️ Stored in MongoDB Atlas
   ✔️ Data table refreshes

2. AI Context Loading
   ✔️ Fetch all MongoDB records
   ✔️ Chunk text
   ✔️ Generate embeddings
   ✔️ Store in ChromaDB
   ✔️ Used as the AI context

3. Ask a Question
   ✔️ User opens the floating chat
   ✔️ Sends a question
   ✔️ Backend finds most relevant chunks
   ✔️ Sends contextual prompt to Claude
   ✔️ Claude answers only from saved text

## 📌 Notes

1. Supports any text input from userupported.
2. Re-embeds data only when DB changes
3. Claude answers strictly from stored MongoDB data
4. The assistant answers strictly from uploaded data.
