import pandas as pd
import cv2
import os


# Step 1: Load the CSV file
csv_file = '../Dataset/ava_v2.2/ava_train_v2.2.csv'
df = pd.read_csv(csv_file, header=None)  # Assuming there are no column names in the CSV

# Step 2: Extract relevant information
video_ids = df[0]
middle_frame_timestamps = df[1]
person_boxes = df[2]
action_ids = df[6]
person_ids = df[7]

#video_ids = ['-5KQ66BBWC4', '-IELREHX_js', '-OyDO1g74vc']
# Step 3: Load video frames
video_folder = '../Dataset/AVA_videos/train/'   # Path to the folder containing the video files

for i in range(len(video_ids)):
    video_id = video_ids[i]
    video_file = os.path.join(video_folder, video_id + '.mp4')
    
    if not os.path.exists(video_file):
        print(f"Video file not found: {video_file}")
        continue
    
    cap = cv2.VideoCapture(video_file)
    
    if not cap.isOpened():
        print(f"Error opening video file: {video_file}")
        continue
    
    middle_frame_timestamp = middle_frame_timestamps[i]
    #person_box = person_boxes[i]
    action_id = action_ids[i]
    person_id = person_ids[i]
    
    # Convert the person_box numpy float64 to a list of float values
    #person_box = person_box.tolist()
    
    frame_timestamp = int(middle_frame_timestamp)  # Convert to integer
    
    cap.set(cv2.CAP_PROP_POS_MSEC, frame_timestamp * 1000)  # Convert frame timestamp to milliseconds
    ret, frame = cap.read()
    
    if not ret:
        print(f"Error retrieving frame at timestamp {frame_timestamp} from video {video_id}")
        cap.release()
        continue
    
    # Process the frame as per your requirement
    # Example: Print the action and person details
    #print(f"Video ID: {video_id}")
    #print(f"Frame Timestamp: {frame_timestamp}")
    #print(f"Person Box: {person_box}")
    #print(f"Action ID: {action_id}")
    #print(f"Person ID: {person_id}")

    save_path = "C:/UB/Summer_2023/DL/Codebase/group-12-deep-learning-final-project/Dataset/AVA_Images/" + str(action_id)
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    save_path  += "/" + video_id + "_" + str(person_id) + ".jpg" 
    #print(save_path)
    # Display the frame
    cv2.imwrite(save_path, frame)
    cv2.waitKey(0)  # Wait for a key press to proceed to the next frame
    
    # Release the video capture object
    cap.release()

cv2.destroyAllWindows()  # Close any open windows
