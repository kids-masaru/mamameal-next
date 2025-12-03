@echo off
echo Checking .env file...
if not exist .env (
    echo Creating .env file from .env.example...
    copy .env.example .env
    echo.
    echo ================================
    echo IMPORTANT: Please edit .env file
    echo and add your GOOGLE_API_KEY
    echo ================================
    echo.
    pause
) else (
    echo .env file already exists.
    echo Make sure it contains GOOGLE_API_KEY=your_key_here
    pause
)
