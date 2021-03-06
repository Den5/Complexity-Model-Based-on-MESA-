Complexity Model

MESA Based Model to Answer the 2018 Spring Complexity Challange, as set out by the Santa Fe Institute.

https://www.complexityexplorer.org/challenges/2-spring-2018-complexity-challenge/submissions


It seems to be losely based on the El Farol problem:

https://en.wikipedia.org/wiki/El_Farol_Bar_problem

Constructive feedback on coding, Agent Based Models, MESA, or Complex systems is welcome.

ToDO:
> Further agent strategy.
> Further improvement to the JavaScript front end.
> More interactive controls and visualizations.


Consider the following system:

Suppose there are fifty (50) agents. At each time step, each agent must decide to
locate at one of three possible pools (investing options) described below. These pools
are called: stable, high, and low. Agents must choose their pool without knowing what
the other agents have picked, and can only rely on information from prior time steps (in
particular, each agent must make their choice knowing only the number of agents (but
not their identity) that located at each pool and each pool's payoff for all prior time steps).
Agents are allowed to switch pools at the start of any time step, but to do so costs the
agent a payment of tau (where 0 <= tau). You are not charged tau for your first choice of
a pool.

Once all agents have selected a pool, each pool provides a payoff for the time step.

� Any agent that locates at the stable pool always receives $1 at the end of the
time step. The other two pools each pay a random amount (see below) that must
be split evenly among all of the agents that selected that particular pool at that
time step. For example, if twenty (20) agents had chosen a pool that paid $40
that period, each agent would receive a payment of $2 ($40/20 agents) for that
period.

The payoffs of the remaining two pools are as follows:

� The high pool pays $80 (that must be split evenly among the residents of that
pool) with probability0.25and $0 otherwise (0.75 probability), and the *low*
pool pays $40 (again, split evenly) with probability 0.5and $0 otherwise (0.5
probability). The random payoffs for the high and low pools are independent of
one another.

The system runs for 100 time steps, with agents accumulating payoffs at each step.

Your challenge is to:

Explore the general dynamics of the above system, using a diverse set of agents, i.e.,
agents that have different rules for deciding which pools to invest in.

Analysis of the System

Your analysis should include (but is not limited to):

� What general behaviors arise in this system? How does the wealth of the agents
change over time? At the aggregate level? At the individual level?
� How does the diversity of strategies influence the dynamics of the system?
� Are there generally classes of agent behavior (say, based on what data they use,
how they process it, or the agent's overall sophistication) that lead to better
performance?
� What happens to the system if you violate one of the original assumptions of the
problem and allow the agents to alter their strategies over time by observing the
performance and strategic details of the other agents?
� Suppose that meta-agents exist that can coordinate the behaviors of a subset of
the agents (and split the resulting payoffs equally across the subset)---how does
this impact the system's behavior?
� How do the answers to the above questions change as:
o tau is altered?
o you change the total number of agents in the world?
