# Asterisco Decoder

## Problem

Brazilian twitter users started hiding certain words from their tweets to obscure their messages, usually to vent or rant in a semi-public manner. Ex: </br>

> \* like ** **** the ***.

For simplicity, we will call these *"asterisk phrases"*.

## Our Solution
Train a machine learning based language model (LM) to predict the most likely words that fill the gaps. Ex: </br>
> I like to feel the sun. </br>
> I like to race the car. </br>
> ...

**OBS.: For the sake of understanding the phrases are in English, but the final goal is to predict phrases that are in Brazilian Portuguese.**

## How it Works
Using the reddit API, we collect a large sample of phrases written in common *"internet language"*. Then, we use these to train an LM on a recurrent neural network (RNN) using the Keras interface. With the trained model, we are able to predict the most likely sentence for any given *"asterisk phrase"*.

## Results

We can't share any results yet because we still haven't finished the LM. We will update when the project is finished.

TODO:

## How to Use

### Training
TODO:

### Predicting
TODO: