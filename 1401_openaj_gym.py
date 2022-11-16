import gym

env = gym.make('LunarLander-v2', render_mode="human")
observation, info = env.reset(seed=42)


def policy(obs):
    return env.action_space.sample()

for _ in range(1000):
    action = policy(observation)
    observation, reward, terminated, truncated, info = env.step(action)
    
    if terminated or truncated:
        observation, info = env.reset()
    
env.close()