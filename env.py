class SQLEnv:
    def __init__(self):
        self.state_data = None

    def reset(self, task="easy"):
        if task == "easy":
            query = "SELECT * FROM users WHERE id = '1 OR 1=1'"
        elif task == "medium":
            query = "SELECT * FROM users WHERE name = 'admin' --'"
        elif task == "hard":
            query = "SELECT * FROM users WHERE id = '1 UNION SELECT password FROM users'"
        else:
            query = "SELECT * FROM users WHERE id = 1"

        self.state_data = {
            "query": query,
            "task": task
        }
        return self.state_data

    def step(self, action):
        query = self.state_data["query"]

        if "OR 1=1" in query or "UNION" in query or "--" in query:
            is_attack = True
        else:
            is_attack = False

        if action == "block":
            reward = 1.0 if is_attack else -0.5
        elif action == "allow":
            reward = -1.0 if is_attack else 0.5
        elif action == "sanitize":
            reward = 0.8 if is_attack else 0.2
        else:
            reward = 0.0

        done = True

        return self.state_data, reward, done

    def state(self):
        return self.state_data