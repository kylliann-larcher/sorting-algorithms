# Sorting Algorithms Visualizer 🧠🎨

This Python project allows you to visualize step-by-step various sorting algorithms using Pygame.  
You can choose the sorting algorithm, the number of elements to sort, and watch in real-time how the data is sorted, with clear animations and an intuitive interface.

🚀 **Features**  
Interactive menu to choose:  
- The sorting algorithm  
- The number of elements  
Dynamic graphical visualization with:  
- Animated vertical bars  
- Action colors (comparison, sorted)  
- Accurate stopwatch  
- Central graduated ruler  
- End message with animation + confirmation sound  
Possibility to:  
- Restart the sort  
- Return to the menu

📦 **Available Algorithms**  
🔁 Bubble Sort  
🪜 Insertion Sort  
🔍 Selection Sort  
🏗 Heap Sort  
🧬 Merge Sort  
🦷 Comb Sort

📁 **Project Structure**  
```
sorting-algorithms/
├── assets/
│   └── done.wav               # Confirmation sound  
├── src/
│   ├── main.py                # Launch the app  
│   ├── menu.py                # Interactive selection menu  
│   ├── display_tri.py         # Pygame graphical interface  
│   ├── animator.py            # Algorithm animation (step by step)  
│   └── sorting.py             # Raw implementations of algorithms  
```

▶️ **Usage**  
1. Install the dependencies  
```bash
pip install pygame
```

2. Run the program  
From the root folder:  
```bash
python src/main.py
```

🛠 **Technologies Used**  
- Python 3  
- Pygame

🙋‍♂️ **Author**  
Perla Assuied, Kyllian Larcher, Alexandre Chevalier

The project was developed as part of my AI specialization at La Plateforme.

🧠 **Future Ideas**  
- Adding a web interface (web visualizer)  
- More algorithms: Radix, Shell, Cocktail...  
- Customization of colors  
- Video export of the sorting process  

📜 **License**  
This project is open-source under the MIT license.
