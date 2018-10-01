#This will help our mouse estimate the value of each
#state, and construct an optimal path to the exit

def TD_learning(env, episodes=100, step_size=0.01, exploration_rate=0.01):
    policy = utils.create_random_policy(env) # Create policy, just for the util function to create Q
    Q = create_state_action_dictionary(env, policy) # 1. Initialize value dictionary formated: { S1: { A1: 0.0, A2: 0.0, ...}, ...}
    
    # 2. Loop through the number of episodes
    for episode in range(episodes): 
        env.reset() # Gym environment reset
        S = env.env.s # 3. Getting State
        A = greedy_policy(Q)[S]  # 4. Deciding on first action
        finished = False
        
        # 5. Looping to the end of the episode
        while not finished:
            S_prime, reward, finished, _ = env.step(A) # 6. Making next step
            A_prime = greedy_policy(Q)[S_prime] # 7. Deciding on second action
            Q[S][A] = Q[S][A] + step_size * (reward + exploration_rate * Q[S_prime][A_prime] - Q[S][A]) # 8. Update rule
            
            # 9. Update State and Action for the next step
            S = S_prime 
            A = A_prime
            
    return greedy_policy(Q), Q
