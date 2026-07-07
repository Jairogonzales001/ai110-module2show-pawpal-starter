# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.
- What classes did you include, and what responsibilities did you assign to each?
For my initial design, I used four main classes: Owner, Pet, Task, and Scheduler. The Owner class keeps track of the owner's information and all of their pets. The Pet class stores basic information about each pet along with its list of tasks. The Task class represents a single pet care activity like feeding, walking, or grooming. The Scheduler class handles the main scheduling logic, such as organizing tasks, sorting them by time, checking for conflicts, and managing recurring tasks.
**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.

As I worked on the project, I made a few changes to my original design. One change was having the Scheduler get tasks directly from the Owner instead of storing its own copy. This made the code cleaner and avoided having duplicate information. I also added recurring task logic so daily and weekly tasks automatically create the next scheduled task after they are completed.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

My scheduler mainly considers the task time, whether the task has been completed, the task frequency, and which pet the task belongs to. I decided that sorting tasks by time was the most important because the goal of the app is to create a daily schedule that is easy to follow.

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

One tradeoff I made was only checking for tasks that happen at the exact same time instead of checking for overlapping time ranges. This keeps the scheduling logic much simpler while still giving the user a warning when there is an obvious conflict.

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

I used AI throughout the project to help me plan the class structure, create the UML diagram, write parts of the code, and fix bugs when something wasn't working. It also helped explain Python features like dataclasses and gave suggestions for writing tests. The most helpful prompts were the ones where I asked AI to explain how different classes should work together instead of just writing the code for me.

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

There were times when I didn't use the AI's suggestion exactly as it was given. For example, it suggested adding more advanced scheduling features that weren't required for this project. I decided to keep the design simpler so it matched the assignment requirements. After using AI's suggestions, I still ran the program and tested everything myself to make sure it worked correctly.

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

I tested several important parts of the program, including marking tasks as complete, adding tasks to pets, sorting tasks by time, creating recurring tasks, and detecting scheduling conflicts. These tests helped confirm that the main features of the scheduler were working as expected.

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

I feel pretty confident that my scheduler works correctly because all of the tests passed and the program produced the expected output during my testing. If I had more time, I would test more edge cases, like invalid time formats, overlapping task durations, and situations with a much larger number of tasks.

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

I think the part that went the best was organizing the project into separate classes. It made the code easier to understand and made it simpler to add new features without changing everything else.

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

If I worked on this project again, I would improve the conflict detection so it could recognize overlapping task times instead of only exact matches. I would also spend more time improving the Streamlit interface to make it more user-friendly.

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?

The biggest thing I learned from this project is that AI can be a really useful tool, but it's still important to understand the code and test everything yourself. AI helped speed up the process, but I still had to make decisions about the design and make sure the final program met the project requirements.
