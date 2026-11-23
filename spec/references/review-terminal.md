# Terminal spec review

````markdown
**Glossary**

1. ```diff
   + Claim
     A reservation that signals intent to give a wishlist item.
   ```

**Behavior**

2. ```diff
   - Restrict who can leave
     Only the event organizer can leave an event.
   ```
3. **Claim visibility**

   ```diff
   - Recipients see who claimed an item for an event as soon as it’s claimed.
   + Recipients see who claimed an item for an event after the event ends.
   ```

   **Why:** This keeps the gift a surprise while helping with thank-you notes.
````
