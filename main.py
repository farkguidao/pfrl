import gym

if __name__ == '__main__':

    # env = gym.make('CartPole-v1')
    # env=gym.make("FrozenLake-v1")
    # env=gym.make("Walker2d-v4")
    # env=gym.make("LunarLander-v2")
    #
    # env.reset()
    # for i in range(1000):
    #     env.render()
    #     observation, reward, done, info = env.step(env.action_space.sample())
    #     if done:
    #         observation = env.reset()
    env = gym.make("ALE/AirRaid-v5",render_mode='human')
    env.reset()
    for i in range(1000):
        # env.render()
        observation, reward, done, info = env.step(env.action_space.sample())
        if done:
            observation = env.reset()
