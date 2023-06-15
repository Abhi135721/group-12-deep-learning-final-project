# Action Detection

## Dataset description
The youtube video ids are in ava_v2.2 folder seperated into train, validation and testing 
Each row contains an annotation for one person performing an action in an interval, where that annotation is associated with the middle frame. Different persons and multiple action labels are described in separate rows.

The format of a row is the following: video_id, middle_frame_timestamp, person_box, action_id, person_id

* video_id: YouTube identifier
* middle_frame_timestamp: in seconds from the start of the YouTube.
* person_box: top-left (x1, y1) and bottom-right (x2,y2) normalized with respect to frame size, where (0.0, 0.0) corresponds to the top left, and (1.0, 1.0) corresponds to bottom right.
* action_id: identifier of an action class, see ava_action_list_v2.2.pbtxt
* person_id: a unique integer allowing this box to be linked to other boxes depicting the same person in adjacent frames of this video.

## Utilities
In the utils folder we have two files 
* **yt_downloader.py**:  
To run this we need to execute the following command and the videos will be downloaded into the location inside Dataset as AVA_videos and subfolders as train, val and test<br />
``` python yt_downloader.py ```
<br /><br />
* **yt_video_get_frames.py**:  
This util parses already downloaded youtube videos and extracts the frames from videos based in the middle_frame_timestamp form the ava csv file. To use this we need to execute the following command.  
``` python yt_video_get_frames.py ```
