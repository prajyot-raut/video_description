PROMPT = """
I am providing a single frame from a video, along with its full transcription.

Your task is to synthesize the visual information from the frame with the contextual information from the text to create a comprehensive, scene-by-scene description of the moment.

### Key Areas for Detailed Description:

1.  **Scene Setting and Visuals:**
    * **Environment:** Describe the location (indoors/outdoors, specific room, etc.). What does the background look like?
    * **Lighting and Color:** What is the dominant lighting (bright, dim, natural, artificial)? What is the overall color palette or mood created by the colors?
    * **Props/Objects:** Identify and describe any significant objects, tools, or items clearly visible in the frame (e.g., a book, a coffee cup, a specific piece of equipment).

2.  **Characters and Action:**
    * **Identification:** Who are the characters present? Describe their appearance (clothing, approximate age, noticeable features).
    * **Action/Movement:** Based on the frame and the transcription, describe the precise action taking place. What is the main subject doing? Is there interaction between characters? Be specific about body language and gestures.
    * **Transcript Context:** How does the dialogue/narration in the transcription relate to or explain the visual action you see? Integrate the text seamlessly into your description of the moment.

3.  **Emotional Tone and Intent:**
    * **Emotions:** Analyze the characters' facial expressions and body language. What specific emotions are being conveyed (e.g., surprise, frustration, joy, focus, suspense)?
    * **Video's Goal:** What is the overall emotional message or tone the video clip is trying to convey to the viewer (e.g., a moment of revelation, a tense argument, a lighthearted joke)?
    * **Embellishment:** Use three relevant emojis that best capture the scene's emotional essence.

---

Start your description here:

Here is the transcription of the video: 
"""
