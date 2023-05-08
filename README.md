# DanPASS

This is not the DanPASS dataset made by [Nina
Grønnum](https://danpass.hum.ku.dk/). Instead this is an adapter that can make
the rifs-CLI work with the data without fuss. We have also made a Train, Dev and
Test split for this data. If you wish to use this dataset, then you first need
to go to [danpass.hum.ku.dk](https://danpass.hum.ku.dk/). Here you will need to
make sure you understand what kind of data this is. Its limitations and bias.

If you decide that this dataset fits you purpose, then feel free to ask [Nina
Grønnum](https://danpass.hum.ku.dk/) for access.

## Intended use

We see this dataset as a small dataset for testing and maybe small scale training.

## Preparing the data

First you need to get access and download the files. These need to be unzip'ed.
Because the original data comes in a format that is not ready for training you have to go through some steps.

### 1. Filesturcture

You have to make sure you extract the files like this:

```

├── all.csv                                          
├── audio                                                                                                  
│   ├── dialogues_mono_soundfiles                                                                          
│   │   └── *.wav                                    
│   └── monologues                                   
│       └── *.wav
├── .gitignore                            
├── README.md                                                                                                                                 ├── text                                                                             
│   ├── dialogues_continuous.txt
│   ├── dialogues_mono_soundfiles         
│   │   └── (Empty for now)                                    
│   ├── monologues_continuous.txt
│   └── monologues                                   
│       └── (Empty for now)                                   
└── text_cleaning.py 

```

### 2. run text\_cleaning.py

dialogues\_continuous.txt and monologues\_continuous.txt contains the text
found in the PDF from the DanPASS page. We have made a script to turn this into
text that can be aligned by the rifs-CLI.
