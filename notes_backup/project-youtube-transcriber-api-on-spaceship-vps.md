---
type: Note
---

**Date: September 17, 2025**
**Final Conclusion: The Root Cause of all failures is that the VPS IP address (209.74.81.185) is being aggressively blocked by YouTube's anti-bot systems.**
This document summarizes the extensive debugging process undertaken to launch the API. The core problem was consistently misdiagnosed as a software or code issue, when the ultimate root cause was a network-level block by YouTube that is insurmountable from the current server.
**Chronological Debugging Path & Failed Hypotheses:**
1.**Initial Setup & Firewall:**
-**Action:** Deployed a basic FastAPI application.
-**Failure:** ERR_CONNECTION_REFUSED.
-**Reason:** The UFW firewall was blocking port 8000.
-**Lesson:** The firewall must be explicitly configured to allow traffic to the application port.
1.**Service Persistence & 502 Errors:**
-**Action:** Configured Nginx as a reverse proxy and set up a systemd service to run the app.
-**Failure:** Repeated 502 Bad Gateway errors.
-**Reasons (Multiple):**
 - The Python virtual environment (venv) was not created or activated correctly.
 - Required Python packages (gunicorn, uvicorn, fastapi) were missing from the venv.
 - The main.py application file was not created or saved correctly.
 - The systemd service file had incorrect paths or permissions.
 - Typos in the Python code (subprocess..CalledProcessError, UnboundLocalError) caused the application to crash on startup.
-**Lesson:** A 502 error indicates the backend application is crashing. The journalctl log is the essential tool for diagnosing the specific Python error causing the crash.
1.**The**youtube-transcript-api** Library (Dead End):**
-**Action:** Attempted to use the youtube-transcript-api Python library.
-**Failure:** Persistent AttributeError messages (get_transcript and list_transcripts not found).
-**Reason:** The library version was fundamentally incompatible or broken. Even after installing a known-good version, it failed silently. This was likely an early symptom of the underlying network block.
-**Lesson:** This library is not reliable for use on a server and should be avoided.
1.**The**yt-dlp** Tool (Correct Tool, Wrong Environment):**
-**Action:** Switched to the industry-standard yt-dlp command-line tool.
-**Failure 1:** The version of yt-dlp installed from the standard Ubuntu (apt) repository was too old (April 2024) and could not communicate with YouTube's modern APIs.
-**Lesson 1:** Always install the latest version of yt-dlp directly from their official GitHub page, not from system package managers.
-**Failure 2:** Persistent Sign in to confirm you’re not a bot error from yt-dlp.
-**Reason:** This is a direct message from YouTube, confirming the IP address block.
-**Lesson 2:** This error is definitive proof of a network-level block.
-**Failure 3:** The API still failed even after providing fresh browser cookies and a valid User-Agent string.
-**Reason:** The verbose log showed that even with valid, authenticated, premium-account cookies, one of YouTube's internal APIs still rejected the request (playability status: LOGIN_REQUIRED).
-**Final Lesson:** The IP block on this server is so severe that it cannot be bypassed with standard authentication methods like cookies or user-agents.**Making direct requests to YouTube from this VPS is not a viable strategy.**
**The Path Forward:**
The only reliable solution is to change the architecture. The request to YouTube must originate from a trusted IP address. The proposed solution is to use a serverless Cloud Function (e.g., Google Cloud Functions, AWS Lambda) as a simple proxy. The VPS will call the Cloud Function, and the Cloud Function will call YouTube. This architecture is standard practice for this type of problem.