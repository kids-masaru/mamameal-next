import subprocess
import sys
import time
import os

print("=" * 50)
print("Mamameal Development Server")
print("=" * 50)
print()

# Check for .env file
if not os.path.exists('.env'):
    print("WARNING: .env file not found!")
    print("Please create a .env file with GOOGLE_API_KEY=your_key_here")
    print()
    input("Press Enter to continue anyway...")

# Start Python Backend
print("Starting Python Backend on port 5328...")
backend = subprocess.Popen(
    [sys.executable, "api/index.py"],
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,
    text=True,
    bufsize=1
)

# Wait a bit for backend to start
time.sleep(2)

# Check if backend is still running
if backend.poll() is not None:
    print("ERROR: Python backend failed to start!")
    print("Output:")
    print(backend.stdout.read())
    input("Press Enter to exit...")
    sys.exit(1)

print("[OK] Python Backend started")
print()

# Start Next.js Frontend
print("Starting Next.js Frontend...")
try:
    npm_cmd = "npm.cmd" if sys.platform == 'win32' else "npm"
    frontend = subprocess.Popen(
        [npm_cmd, "run", "dev"],
        creationflags=subprocess.CREATE_NEW_CONSOLE if sys.platform == 'win32' else 0
    )
    
    print("[OK] Next.js Frontend started in new window")
    print()
    print("=" * 50)
    print("Servers are running!")
    print("Frontend: http://localhost:3000")
    print("Backend: http://localhost:5328")
    print("=" * 50)
    print()
    print("Press Ctrl+C to stop all servers...")
    
    # Keep script running and show backend output
    for line in backend.stdout:
        print(f"[Backend] {line}", end='')
        
except KeyboardInterrupt:
    print("\nShutting down...")
    backend.terminate()
    frontend.terminate()
    print("Servers stopped.")
