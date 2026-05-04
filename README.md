\# Localization Audio Pipeline Demo



!\[Unreal Demo Overview](images/unreal-demo-overview.png)



A technical audio and localization pipeline demo for game dialogue, built around English/Spanish VO asset management, Python automation, Wwise localization, and Unreal Engine implementation.



\## Overview



This project demonstrates a complete EN/ES localization audio pipeline for game dialogue, from dialogue organization to in-engine playback.



The demo simulates a Life Simulation game environment with interactive dialogue stations, system sounds, ambience testing, and runtime language switching between English and Spanish.



\## Tools Used



\- Reaper

\- iZotope RX

\- Microsoft Excel

\- Python

\- Audiokinetic Wwise

\- Unreal Engine 5



\## Pipeline



1\. Dialogue creation and organization in Excel

2\. Voice recording and editing in Reaper

3\. Audio cleanup in iZotope RX

4\. File naming and organization using Python

5\. Localized VO setup in Wwise

6\. Interactive playback testing in Unreal Engine



\## Project Scope



Languages:



\- English

\- Spanish



Characters:



\- Male Adult

\- Female Adult

\- System / Narrator



Dialogue categories:



\- Greeting

\- Complaint

\- Work

\- Idle

\- Reaction

\- Objective

\- System



\## Naming Convention



The project uses a structured VO naming convention:



VO\_<Language>\_<Character>\_<Category>\_<LineType>\_<ID>\_<Variation>.wav



VO\_EN\_FA\_Work\_Q\_003\_A.wav

VO\_ES\_FA\_Work\_Q\_003\_A.wav



\## Python Automation



Python scripts were used to automate parts of the pipeline, including:



Generating standardized file names

Reading dialogue metadata from Excel

Copying and organizing audio files

Preparing localized folders for Wwise import

Wwise Implementation



\## The Wwise setup includes:



English and Spanish localized sources

Shared voice objects

Organized dialogue containers

VO event playback

SoundBank generation

Unreal Engine integration

Unreal Engine Demo



\## The Unreal demo scene includes:



Interactive dialogue stations

Language switching

UI and system sound testing

Ambience testing

Wwise event triggering through Unreal

Documentation



Additional project documentation is available in the docs/ folder:



00\_project\_foundation.pdf

01\_localization\_audio\_pipeline.pdf

02\_dialogue\_interaction\_dataset.pdf



Author



Created by Pablo Flores Alosi

Sound Designer / Technical Audio Designer

Valencia, Spain



Portfolio: https://pablofalosi.wixsite.com/home

LinkedIn: https://www.linkedin.com/in/pablofloresalosi/

GitHub: https://github.com/PabloFloresAlosi



