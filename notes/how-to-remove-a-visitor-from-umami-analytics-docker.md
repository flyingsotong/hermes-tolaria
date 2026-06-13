---
type: Personal-Note
---

**Step 1: Access the Database** 
SSH into the server and navigate to the docker directory:

```
cd umami-docker/
```

**Step 2: Enter the Postgres Console** 
Run the following command to log into the database container:

```
docker compose exec db psql -U umamiuser -d umamiproject
```


**Step 3: Delete the Session** 
Replace \THE_SESSION_ID\ with the ID you want to remove (e.g., \bae5f258-4f6a-5ee3-8dec-bf9c5a2dc366\). _Note: This automatically deletes associated pageviews and events._

```
DELETE FROM website_event 
WHERE session_id = '2446b22b-a147-5ce2-a7c3-b318f86f9784';
```