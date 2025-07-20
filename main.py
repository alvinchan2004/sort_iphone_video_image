import os
import shutil

base_path = r"\\\192.168.1.2\photo\MobileBackup"
month_names = [f"{i:02d}" for i in range(1, 13)]  # "01" to "12"

# Recursively read all folders
for root, dirs, files in os.walk(base_path):
    # Only process folders named "01" to "12"
    if os.path.basename(root) in month_names:
        image_folder = os.path.join(root, "图片")
        video_folder = os.path.join(root, "录像")
        live_folder = os.path.join(root, "live")
        os.makedirs(image_folder, exist_ok=True)
        os.makedirs(video_folder, exist_ok=True)
        os.makedirs(live_folder, exist_ok=True)
        print(f"Created 'image', 'video', and 'live' in: {root}")

        for f in files:
            if f.lower().endswith(".mov"):
                mov_path = os.path.join(root, f)
                # Check for matching image in supported formats
                image_found = False
                for ext in [".heic", ".jpg", ".png"]:

                    image_name = os.path.splitext(f)[0] + ext
                    image_path = os.path.join(root, image_name)
                    if os.path.exists(image_path):
                        # Move only live mov to 'live'
                        shutil.move(mov_path, os.path.join(live_folder, f))
                        print(f"Moved {f} to 'live' in: {root}")
                        image_found = True
                        break
                if not image_found:
                    # Move .mov to 'video'
                    dst_path = os.path.join(video_folder, f)
                    if not os.path.exists(dst_path):
                        shutil.move(mov_path, dst_path)
                        print(f"Moved {f} to 'video' in: {root}")
        for f in files:
            if f.lower().endswith((".heic", ".jpg", ".png")):
                # Move image to 'image'
                src_path = os.path.join(root, f)
                dst_path = os.path.join(image_folder, f)
                shutil.move(src_path, dst_path)
                print(f"Moved {f} to 'image' in: {root}")

        print("finished processing folder:", root)

print("All folders processed successfully.")