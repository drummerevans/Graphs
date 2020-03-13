## panda_data.py

This program takes ADS-B data from a .csv file and extracts relevant information to another .csv file.

In this intance it extracts, roll angle, track rate, ground speed, air speed and alitude.
It then outputs all of this data for aircraft with either both roll and track zero or both non-zero.
In addition to this, the program calcaultes the track rate using the RHS of the centripetal force equation:

$g \frac{\tan{\phi}{v_A}} \times \frac{180}{\pi}$

To run use:
```bash
python panda_data.py
```

## roll_plot.py

This generates a plot of the measured track angle rate against the one calculated using the relation:

$g \frac{\tan{\phi}{v_A}} \times \frac{180}{\pi}$

from data obtained from 'panda_data.py'. If the laws of Physics are obeyed, they should all line on a the straight line...
This acts as a quality check to obtain aircraft without any 'rogue' data emissions.

To run use:
```bash
python roll_plot.py
```

## opencv_object_tracking.py

This program tracks a video image and outputs the x and y co-ordinates of the top-left corner of the slector box to a .csv file. 
In addition, it also outputs the width and height of the tracker box to the same .csv file.

To run use:
To run use:
```bash
python opencv_object_tracking.py -v MyVideo.mp4 -t csrt
```

Then use the following to analyse the video,
1. press s  - to start tracking
2. draw a box using the mouse around desired object.
3. press space bar to continue video
4. press q to quit early