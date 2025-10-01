# 🧭 Maze Navigation with Bug Algorithm (ROS 2 + Gazebo)

This project implements a simple **robot maze navigation** demo using the **Bug Algorithm** within ROS 2 and Gazebo.  
The robot navigates through a maze world while avoiding walls, demonstrating basic **autonomous navigation** concepts.  

---

## 📂 Project Structure
```bash
maze_navigation/
│── maze_navigation/
│ ├── init.py
│ ├── bug_algorithm.py # Python node implementing Bug Algorithm
│── launch/
│ └── maze_navigation.launch.py # Launch file to start Gazebo + node
│── world/
│ └── maze_world.world # Custom Gazebo maze environment
│── README.md
│── requirements.txt
```
---

## 🚀 Features
- Implements **Bug Algorithm** for obstacle avoidance.
- Custom **Gazebo maze world** with walls.
- ROS 2 node (`bug_algorithm.py`) subscribes to laser scan data and publishes velocity commands.
- Modular launch file for running simulation.

---

## ⚙️ Requirements
- **ROS 2 Humble** (or newer)
- **Gazebo Fortress / Classic**
- `geometry_msgs`, `sensor_msgs`, `nav_msgs`
- Python 3.8+

- Install dependencies:

```bash
rosdep install --from-paths src --ignore-src -r -y
```

- Python dependencies (optional):
```bash
pip install -r requirements.txt
```
---

## ▶️ How to Run

Build your workspace:

```bash
cd ~/ros2_ws
colcon build
source install/setup.bash
```

Launch simulation:
```bash
ros2 launch maze_navigation maze_navigation.launch.py
```
---

## 📖 Bug Algorithm (Quick Summary)

The Bug Algorithm is a simple motion planning method:

1. Move toward the goal until an obstacle is detected.

2. Follow the obstacle boundary until the path to the goal is clear again.

3. Repeat until the robot reaches the goal or determines it’s trapped.

---

## 📸 Demo (Optional GIF/Screenshot)

![Demo GIF](docs/demo.gif)

---

## 🛠 Future Improvements

- Add vision-based wall detection.

- Use proximity sensors instead of laser scans.

- Extend to Bug2 / TangentBug algorithms.

- Compare with ROS 2 Nav2 navigation stack.

---

## 👨‍💻 Author
```bash
Created by Sunday Ikechukwu
GitHub: [Precious-Weal5699](https://github.com/Precious-Weal5699)
```