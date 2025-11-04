# Mathematical Models for Typhoon Signal Analysis

## Regression Analysis
- **Linear Regression**: Predict typhoon signal timing using meteorological variables (wind speed, pressure, rainfall)
- **Logistic Regression**: Model signal escalation decisions (T1→T3→T8→T9→T10) based on weather conditions
- **Time Series Regression**: Analyze signal duration and frequency patterns over typhoon seasons
- **Multiple Regression**: Evaluate factors affecting signal accuracy (forecast accuracy, historical data, public safety)
- **Survival Analysis**: Model time-to-signal-change based on typhoon intensity and trajectory
- **Regional Comparative Regression**: Compare signal timing between Hong Kong and Macau using cross-jurisdictional data

## Simulation Models
- **Monte Carlo Simulation**: Model typhoon path uncertainty and signal decision outcomes
- **Weather Simulation**: Simulate typhoon development and intensity changes
- **Decision Tree Simulation**: Model signal escalation logic under different weather scenarios
- **Impact Simulation**: Model economic and social impacts of different signal timing decisions
- **Risk Assessment Simulation**: Evaluate signal accuracy and false positive/negative rates
- **Storm Surge Simulation**: Delft3D-FLOW modeling for storm surge height prediction and coastal flooding
- **Cross-Border Coordination Simulation**: Model regional warning system coordination between jurisdictions

## Advanced Modeling Approaches (Based on Takagi et al., 2018)

### Storm Surge and Hydrodynamic Modeling
- **Delft3D-FLOW Integration**: Couple typhoon models with hydrodynamic simulation for storm surge prediction
- **Parametric Typhoon Models**: Myers formula for pressure distribution around typhoon center
- **Shallow-Water Wave Models**: Simulate long waves (storm surges, tsunamis, tidal propagation)
- **Wave Overtopping Models**: Assess wave runup and overtopping in coastal areas
- **Breaking-Wave Setup Models**: Calculate wave-induced water level changes using Goda (2000) equations

### Regional Comparative Analysis
- **Cross-Jurisdictional Signal Timing**: Compare warning signal issuance timing between Hong Kong and Macau
- **Economic Impact Modeling**: Assess regional economic impacts of different warning timing decisions
- **Forward Speed Analysis**: Model typhoon forward speed impact on warning timing (e.g., Hato's 32.5 km/h vs. historical 16 km/h)
- **Pressure Drop Modeling**: Analyze atmospheric pressure differences between regions during typhoon passage

### Historical Pattern Analysis
- **70-Year Track Analysis**: JTWC Best Track Data analysis for Pearl River Delta typhoon patterns
- **Category 1+ Typhoon Analysis**: Focus on storms affecting Macau and Hong Kong over decades
- **Landfall Pattern Recognition**: Identify common trajectories (ESE to WNW) and their impact patterns
- **Forward Speed Comparison**: Historical analysis of typhoon forward speeds and their warning implications

## Data Requirements

### For Regression Analysis
- **Historical typhoon data**: 70+ years of JTWC Best Track Data
- **Signal records**: Hong Kong and Macau warning signal history
- **Meteorological data**: Wind speed, pressure, rainfall, temperature
- **Economic impact data**: Regional economic impact assessments
- **Cross-border data**: Comparative regional warning system data

### For Simulation Models
- **Real-time weather data**: HKO and Macau meteorological data
- **Typhoon tracking data**: JTWC and JMA Best Track Data
- **Signal decision logs**: Historical warning signal decisions and timing
- **Impact assessments**: Economic and social impact evaluations
- **Regional coordination data**: Cross-jurisdictional warning system coordination

### For Advanced Storm Surge Modeling
- **Bathymetry data**: GEBCO (General Bathymetric Chart of the Oceans) data
- **Computational domain**: Pearl River Delta region (20.0°N–111.0°E to 23.0°N–116.0°E)
- **Grid resolution**: 0.01° spatial grid (~1km resolution)
- **Tidal data**: Astronomical tide data for storm surge validation
- **Field survey data**: Post-typhoon inundation measurements and witness accounts

### For Regional Comparative Analysis
- **Cross-border meteorological data**: Hong Kong and Macau weather station data
- **Economic impact data**: Regional economic impact assessments
- **Warning system criteria**: Official criteria from both jurisdictions
- **Timing analysis data**: Signal issuance timing comparisons
- **Coordination data**: Cross-jurisdictional coordination mechanisms

## Model Validation and Verification
- **Pressure Comparison**: Observed vs. calculated surface pressures (±5hPa accuracy)
- **Storm Surge Validation**: Simulated vs. observed storm surge heights at Shek Pik
- **Field Survey Validation**: Post-typhoon field measurements vs. model predictions
- **Cross-Reference Validation**: Multiple data sources for accuracy verification
- **Regional Validation**: Cross-jurisdictional model performance assessment
