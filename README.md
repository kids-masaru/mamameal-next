# Mamameal Next (Vercel + Gemini)

This is the modernized version of the Mamameal PDF conversion tool, designed for Vercel deployment and using Google Gemini API for high-accuracy data extraction.

## Features
- **Frontend**: Next.js (React) with Tailwind CSS.
- **Backend**: Python Serverless Functions (Flask) on Vercel.
- **AI**: Google Gemini API (`gemini-1.5-pro`) for PDF analysis.
- **UI**: Modern drag-and-drop interface with custom SVG icons.

## Prerequisites
- Node.js
- Python 3.9+
- Vercel CLI (`npm i -g vercel`)
- Google Gemini API Key

## Setup & Deployment

1.  **Install Dependencies**
    ```bash
    cd mamameal-next
    npm install
    ```

2.  **Local Development**
    - You need to run both Next.js and the Python API.
    - It's recommended to use Vercel CLI for local dev to handle the Python serverless functions.
    ```bash
    vercel dev
    ```
    *Note: You must set `GOOGLE_API_KEY` in your `.env` file or Vercel project settings.*

3.  **Deploy to Vercel**
    ```bash
    vercel deploy
    ```

4.  **Environment Variables**
    - Go to your Vercel Project Settings > Environment Variables.
    - Add `GOOGLE_API_KEY` with your Gemini API key.

## Project Structure
- `app/`: Next.js Frontend code.
- `api/`: Python Backend code (`index.py`).
- `api/assets/`: Excel templates and Master CSV files.
- `components/`: React components (Icons, etc.).
