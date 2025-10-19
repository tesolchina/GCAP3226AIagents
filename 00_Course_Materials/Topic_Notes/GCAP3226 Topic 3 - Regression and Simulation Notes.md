# GCAP3226 Topic 3: Bus Routes Coordination - Regression and Simulation Modeling

> **Topic**: [[GCAP3226-Topic3-BusRoutesCoordination]]
> **Focus**: Game theory and optimization for inter-operator collaboration
> **Date**: September 26, 2025

## Overview
Bus route coordination between competing operators (272A-KMB and 582-CityBus) presents a complex multi-agent optimization problem requiring game theory, demand modeling, and strategic simulation to identify mutually beneficial coordination strategies.

## 📊 Regression Analysis Applications

### 1. Demand Prediction Models
**Time-Series Regression Framework:**
```
Demand_{i,t} = β₀ + β₁(Time_of_Day) + β₂(Day_of_Week) + β₃(Weather) + β₄(Competitor_Service) + β₅(Price) + AR(1) + ε
```

**Where:**
- i = bus stop index (1 to 8 shared stops)
- t = time period (15-minute intervals)

**Key Variables:**
- **Dependent**: Passenger boarding counts by operator and stop
- **Independent**: Service frequency, arrival times, fare differences, weather conditions
- **Lagged Variables**: Previous period demand, competitor actions
- **Seasonal Controls**: Holiday effects, school calendar, special events

**Expected Relationships:**
- Negative correlation between operators' demand (substitution effect)
- Positive relationship between service frequency and ridership
- Weather-dependent demand variations by route characteristics

### 2. Revenue Impact Analysis
**Multi-Level Mixed Effects Model:**
```
Revenue_{operator,stop,day} = γ₀ + γ₁(Coordination_Strategy) + γ₂(Service_Level) + γ₃(Competition_Intensity) + u_{stop} + v_{day} + ε
```

**Coordination Strategy Variables:**
- Complementary scheduling indicator (0/1)
- Time-gap between services (continuous)
- Peak/off-peak responsibility sharing (categorical)
- Joint marketing initiatives (0/1)

**Control Variables:**
- Route characteristics (distance, stops, travel time)
- Catchment area demographics
- Alternative transport availability
- Seasonal and temporal controls

### 3. Service Quality Regression
**Passenger Satisfaction Model:**
```
Satisfaction = β₀ + β₁(Waiting_Time) + β₂(Service_Reliability) + β₃(Coordination_Quality) + β₄(Information_Availability) + ε
```

**Service Quality Metrics:**
- Average waiting times at shared stops
- Service reliability (on-time performance)
- Information coordination (real-time updates)
- Passenger comfort (crowding, seat availability)

**Coordination Quality Indicators:**
- Schedule synchronization effectiveness
- Information system integration
- Joint problem resolution responsiveness
- Service disruption coordination

## 🎯 Simulation Modeling Applications

### 1. Game Theory Simulations
**Multi-Agent Strategic Interaction Model:**

**Players**: KMB (272A) and CityBus (582)
**Strategies**: 
- Service frequency decisions
- Schedule timing choices
- Coordination participation levels
- Price/fare adjustments

**Payoff Functions:**
```
Π_KMB = Revenue_KMB - Cost_KMB - Coordination_Cost + Reputation_Benefit
Π_CityBus = Revenue_CityBus - Cost_CityBus - Coordination_Cost + Reputation_Benefit
```

**Simulation Scenarios:**
1. **Non-Cooperative Game**: Each operator optimizes independently
2. **Cooperative Game**: Joint optimization with benefit sharing
3. **Sequential Game**: One operator leads, other responds
4. **Repeated Game**: Long-term strategic interactions with reputation effects

**Nash Equilibrium Analysis:**
- Identify stable strategy combinations
- Assess coordination sustainability
- Evaluate welfare improvements from cooperation

### 2. Schedule Optimization Simulation
**Genetic Algorithm Framework:**
```
Chromosome: [Departure_Times_KMB, Departure_Times_CityBus]
Fitness Function: f(x) = Passenger_Welfare + Operator_Profit - Coordination_Cost
```

**Optimization Constraints:**
- Minimum service frequency requirements
- Fleet capacity limitations
- Driver scheduling constraints
- Regulatory compliance requirements

**Simulation Process:**
1. Initialize population of schedule combinations
2. Evaluate fitness based on passenger waiting times and operator costs
3. Apply genetic operators (crossover, mutation, selection)
4. Iterate until convergence to optimal schedules

**Performance Metrics:**
- Average passenger waiting time reduction
- Operator cost savings or revenue improvements
- Service reliability improvements
- System-wide efficiency gains

### 3. Passenger Choice Modeling
**Discrete Choice Simulation:**
```
Utility_{passenger,route} = V + ε
V = β₁(Travel_Time) + β₂(Waiting_Time) + β₃(Fare) + β₄(Comfort) + β₅(Reliability)
```

**Agent-Based Passenger Behavior:**
- **Individual Attributes**: Age, income, time sensitivity, route familiarity
- **Choice Process**: Route selection based on expected utility
- **Learning Behavior**: Adaptation to service changes over time
- **Information Usage**: Response to real-time information systems

**Simulation Scenarios:**
- Impact of coordinated vs. uncoordinated schedules on route choice
- Passenger adaptation to new coordination strategies
- Welfare distribution effects across different passenger types

### 4. System Dynamics Models
**Long-Term Strategic Simulation:**

**Feedback Loops:**
- Service Quality → Ridership → Revenue → Service Investment → Service Quality
- Coordination Success → Trust → Cooperation Willingness → Coordination Success
- Competition Intensity → Service Innovation → Customer Satisfaction → Market Share

**Stock and Flow Variables:**
- **Stocks**: Ridership levels, operator reputation, infrastructure quality
- **Flows**: Passenger acquisition/loss, service improvements, coordination initiatives

**Policy Scenarios:**
1. Regulatory mandated coordination
2. Voluntary cooperation with incentives
3. Market-based competition with minimal intervention
4. Public-private partnership coordination models

## 🔧 Technical Implementation

### Data Collection Requirements
**Primary Data Sources:**
- Route 272A ridership data (KMB)
- Route 582 ridership data (CityBus)
- Passenger journey data at 8 shared stops
- Service schedule and delay data
- Customer satisfaction surveys

**External Data:**
- Weather data for demand modeling
- Special events calendar
- Alternative transport service levels
- Demographic data for catchment areas

**Real-Time Data Streams:**
- GPS tracking for both routes
- Passenger counting systems
- Traffic condition monitoring
- Mobile app usage data

### Software Implementation
**Statistical Analysis:**
- R: `lme4` for mixed effects models, `forecast` for time series
- Python: `statsmodels`, `sklearn` for machine learning approaches
- STATA: Panel data analysis and econometric modeling

**Game Theory Simulation:**
- Python: Custom multi-agent simulation framework
- NetLogo: Agent-based strategic interaction models
- MATLAB: Game theory toolbox for equilibrium analysis

**Optimization:**
- Python: `DEAP` for genetic algorithms, `cvxpy` for convex optimization
- R: `GA` package, `optim()` for schedule optimization
- Commercial: IBM CPLEX for large-scale optimization problems

### Model Validation
**Cross-Validation Approach:**
- Split data into training/testing periods
- Validate demand predictions against historical data
- Test game theory predictions with pilot coordination programs
- Calibrate passenger choice models with revealed preference data

## 📈 Policy Applications

### Regulatory Framework Design
**Evidence-Based Policy Recommendations:**
1. **Coordination Incentives**: Optimal subsidy structures to encourage cooperation
2. **Service Standards**: Minimum service level requirements under coordination
3. **Information Sharing**: Data transparency requirements between operators
4. **Performance Monitoring**: KPIs for coordination success measurement

### Implementation Strategy
**Phased Rollout Plan:**
1. **Pilot Phase**: Test coordination at 2-3 shared stops with full monitoring
2. **Evaluation Phase**: Assess pilot results using regression analysis
3. **Optimization Phase**: Refine coordination strategies based on findings
4. **Scale-Up Phase**: Expand to all 8 stops with continuous monitoring

### Stakeholder Benefits Quantification
**For Transport Department:**
- System efficiency improvements (reduced deadhead, optimized capacity)
- Passenger welfare gains (reduced waiting times, improved service)
- Regulatory compliance cost reductions

**For Bus Operators:**
- Revenue optimization under coordination scenarios
- Cost savings from operational efficiency
- Risk assessment for different coordination models

**For Passengers:**
- Service quality improvements quantification
- Travel time savings estimation
- Service reliability enhancements

## 🎯 Expected Research Outcomes

### Quantitative Deliverables
**Performance Metrics:**
- 15-25% reduction in average passenger waiting times
- 5-10% improvement in operator profitability through coordination
- 20-30% reduction in service variability at shared stops

**Economic Analysis:**
- Net present value of coordination benefits over 5-year horizon
- Break-even analysis for coordination program implementation
- Sensitivity analysis for key assumptions and parameters

### Strategic Recommendations
**Optimal Coordination Models:**
1. **Complementary Scheduling**: Alternate departures to minimize passenger waiting
2. **Peak/Off-Peak Division**: Operator specialization by time periods
3. **Dynamic Coordination**: Real-time schedule adjustments based on demand
4. **Service Integration**: Joint ticketing and information systems

### Methodological Contributions
- Multi-operator coordination optimization framework
- Game theory applications to public transport planning
- Integration of passenger choice modeling with operator strategy simulation
- Policy design methodology for competitive market coordination

---

## 🔗 Related Resources
- [[GCAP3226-Topic3-BusRoutesCoordination]] - Main topic overview
- [[topic selection and group formation]] - Course context
- **Technical Tools**: Game theory software, optimization platforms
- **Data Sources**: KMB, CityBus operational data, Transport Department statistics

*This framework transforms inter-operator coordination from informal agreements into scientifically designed, mutually beneficial strategic partnerships supported by rigorous quantitative analysis.*