# The Asian Hate Tracker Project

## Introduction
As two people of Asian descent experiencing the global COVID-19 pandemic in New York City, we felt we were constantly hearing stories from our fellow Asian classmates about hate-based incidents--the derogatory message left on a Columbia whiteboard, an angry side-comment of a passerby telling us to "go back," the suddenly cleared hole in subway space from neighbors scared to touch you. We wanted a way to document these stories and more importantly, we wanted a way to measure this very real racial backlash that seems to follow not only this pandemic, but a history of epidemics and diseases. In a time when we are being told to rely on data, we wanted to use that data to give these stories another dimension, to illustrate just how concrete and palpable the increase in racial tension is. 
## Data
For our data, we wanted to analyze a social-media platform in order to gauge sentiment towards Asians, however most social media platforms we considered (Facebook, Twitter, Instagram) both did not allow unrestricted access to their data and did not fully anonymize their users. As such we drew inspiration from past work like Vice's  [article](https://www.vice.com/en_us/article/d3nbzy/we-analyzed-more-than-1-million-comments-on-4chan-hate-speech-there-has-spiked-by-40-since-2015), and focused our analysis on data from the image-board site 4chan, which allowed for anonymous users and unrestricted access to their data. 4chan also conveniently has an archive site, 4plebs, which archives posts from the /pol board (which stands for politically incorrect and which all our analysis is done off of).

## Analysis
For the analysis of the data, we once again took inspiration from the Vice 2019 article and decided to gauge racial-tension through the frequency of hate-terms which were classified as "Asian" hate-terms.
For this dictionary, we used [HateBase](https://hatebase.org/), which provides a free API and access to different classification of hate-terms. We decided to use this dictionary because it is widely used in academia and media. We also manually cleaned out any terms which were either outdated or had been recycled into a different meaning. One drawback to this approach is that the database itself was missing certain obvious racial epithets that are in circulation today.

We chose to do text analysis and ran a script which would go through the data, and count the number of posts that in a given day contained "Asian" hate terms, to see how many times such terms were used on /pol and to see if there were any correlations with the pandemic timing.

## Future work
In order to strengthen our analysis, we would like to finely and manually comb through the posts that our programs classified as "containing hate-speech" to see if there is any additional data to be gleaned from these posts, as well as to rule out any confounding event besides the pandemic that could be causing the increase in hate-speech.
