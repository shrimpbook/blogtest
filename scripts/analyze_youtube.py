import os
from youtube_transcript_api import YouTubeTranscriptApi

# Define video IDs
VIDEO_IDS = ['VIDEO_ID_1', 'VIDEO_ID_2', 'VIDEO_ID_3']

def fetch_transcript(video_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        transcript_text = ' '.join([entry['text'] for entry in transcript])
        return transcript_text
    except Exception as e:
        return f"Error fetching transcript for {video_id}: {str(e)}"

def analyze_transcripts(transcripts):
    # Implement your transcript analysis logic here
    analysis = "Analysis of transcripts:\n\n" + "\n\n".join(transcripts)
    return analysis

def generate_markdown(analysis):
    content = f"""---
title: Analysis of YouTube Videos
date: 2025-02-10
categories: YouTube Analysis
---

{analysis}
"""
    return content

def save_markdown(content, filename):
    with open(filename, 'w') as file:
        file.write(content)

if __name__ == "__main__":
    transcripts = [fetch_transcript(video_id) for video_id in VIDEO_IDS]
    analysis = analyze_transcripts(transcripts)
    markdown_content = generate_markdown(analysis)
    save_markdown(markdown_content, os.path.join('_posts', '2025-02-10-analysis.md'))
