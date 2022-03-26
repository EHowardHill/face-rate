# I asked hundreds of people to rate the relative attractiveness between pairs of AI-generated faces. This is what I learned.

## Overview and Primary Results

On a whim, I thought it might be a fun project to download hundreds of AI-generated faces for a social experiment. About 661 faces to be exact. I set up a website in which I had people select between randomized pairs of faces, which one seemed to be more 'attractive' to them. I optionally allowed people to select whether they had an attraction to Men, Women, both, or neither, as well as a box to collect their age. A random ID was used to identify repeat voters, but it has no other data associated with it.

I sent out a link to Reddit, Instagram, and several Discord servers I'm a part of. Here are some of the base level statistics:

- I collected **7524** votes from **223** individual people.
- **85** people liked men, **148** liked women, **39** liked both, and **40** either liked neither or opted not to disclose.
- The ages of contributors ranged from **15** to **56** years old.
- The age that contributed the most votes were from those aged **20** years old.

## Most Popular (All Categories)

The most popular face among all categories was photo **No.53**, which ranked **#4 among people who like men** and **#3 among people who like women**.

![No.53](https://github.com/EHowardHill/face-rate/blob/main/static/53.jpg?raw=true)

The highest rated male face among all categories is **No.235** at overall position **#10**, which ranked **#9 among people who like men** and **#21 among people who like women**.

![No.235](https://github.com/EHowardHill/face-rate/blob/main/static/235.jpg?raw=true)

## Most Popular (People who like men)

The most popular face among people who like men was photo **No.99**, which ranked **#60 among people who like women**.

![No.99](https://github.com/EHowardHill/face-rate/blob/main/static/99.jpg?raw=true)

The highest rated male faces (2 were tied) among people who like men were photos **No.547** and **No.187**, at position **#2**. Neither photos ranked among people who like women.

No.547:
![No.547](https://github.com/EHowardHill/face-rate/blob/main/static/184.jpg?raw=true)

No.187:
![No.187](https://github.com/EHowardHill/face-rate/blob/main/static/547.jpg?raw=true)

## Most Popular (People who like women)

The most popular face among people who like women was photo **No.420**, which ranked **#38 among people who like men**.

![No.420](https://github.com/EHowardHill/face-rate/blob/main/static/420.jpg?raw=true)

The highest rated male face among people who like women is photo **No.489**, which was ranked at **#11**. It ranked as **#27** among people who like men.

![No.489](https://github.com/EHowardHill/face-rate/blob/main/static/489.jpg?raw=true)

## Demographic Statistics##

Each of the photos was classified into **college-age (<25)**, **young adult (25-32)**, **adult (32-43)**, **older adult (44-53)**, or **senior (54-100)**. Sex and age detected was handled by an open-cv-based age detection algorithm.

Women recieved **379** total votes.
Men recieved **94** total votes.

Of the top **25** results overall, there were:
- **16** women
- **9** men
- **13** college-age
- **7** young adult

Among people who like men:
- **11** women
- **9** men
- **8** college-age
- **10** young adult
- **1** adult

Among people who like women:
- **16** women
- **4** men
- **11** college-age
- **9** young adult

##Statistical Analysis##

- All faces were voted on at least once. This means that no matter what you look like, someone thinks you're a good option :)
- **People who like men** tend to find **both men and women** to be attractive, while **people who like women** tend to favor women.
- While **the percieved attractiveness of women tends to be agreed on** by both sides, **the percieved attractiveness of men** varies wildly.
- **People who like women are slightly more attracted to the 18-25 demographic** than people who like men by approx. 137.5%.
- Women are **403.19% more likely** to be voted as attractive than men.

##Conclusion##

No conclusion, I did this just for fun.
