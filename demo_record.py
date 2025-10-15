import time, pyautogui, os
from datetime import datetime

def record_demo(duration=60, output="demo.mp4"):
    print("Starting demo recording in 5 seconds...")
    time.sleep(5)
    print("Recording... (move your mouse naturally or show the app in browser)")
    pyautogui.alert("Demo recording starting now — interact with the app!")
    start_time = time.time()
    screenshots = []
    while time.time() - start_time < duration:
        screenshot = pyautogui.screenshot()
        screenshots.append(screenshot)
        time.sleep(0.5)  # 2 FPS
    print("Recording complete. Saving as MP4...")
    folder = "demo_frames"
    os.makedirs(folder, exist_ok=True)
    for i, img in enumerate(screenshots):
        img.save(f"{folder}/frame_{i:04d}.png")
    os.system(f"ffmpeg -r 2 -i {folder}/frame_%04d.png -vcodec libx264 -pix_fmt yuv420p {output}")
    print(f"Demo saved as {output}")

if __name__ == "__main__":
    record_demo(duration=60, output="demo.mp4")
