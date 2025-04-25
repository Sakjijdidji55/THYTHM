import cv2
import os


def extract_frames(video_path, output_folder):
    # 检查输出文件夹是否存在，如果不存在则创建
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 打开视频文件
    cap = cv2.VideoCapture(video_path)

    # 检查视频是否成功打开
    if not cap.isOpened():
        # print("Error opening video file")
        return

    frame_count = 0
    while True:
        # 读取一帧
        ret, frame = cap.read()

        # 如果读取失败，说明视频结束，退出循环
        if not ret:
            break

        # 构建保存帧的文件名
        frame_filename = os.path.join(output_folder, f"frame_{frame_count:04d}.png")

        # 保存当前帧为 JPEG 图像
        cv2.imwrite(frame_filename, frame)

        frame_count += 1
        

    # 释放视频捕获对象
    cap.release()
    print(f"Extracted {frame_count} frames successfully.")


if __name__ == "__main__":
    # 替换为你的视频文件路径
    video_path = "D:\\pythongame\\video\\4月7日(3).mp4"
    # 替换为你想要保存帧的文件夹路径
    output_folder = "./switch"
    extract_frames(video_path, output_folder)
    