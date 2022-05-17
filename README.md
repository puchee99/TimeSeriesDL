<div id="top"></div>

<!-- PROJECT SHIELDS -->
<!--
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/puchee99/TimeSeriesDL">
    <img src="images/pytorch.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">TimeSeriesDL</h3>

  <p align="center">
    TimeSeries analysis and DL.
    <br />
    <a href="https://github.com/puchee99/TimeSeriesDL"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/puchee99/TimeSeriesDL">View Demo</a>
    ·
    <a href="https://github.com/puchee99/TimeSeriesDL/issues">Report Bug</a>
    ·
    <a href="https://github.com/puchee99/TimeSeriesDL/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## About The Project

The objective of this project is to 

![product-screenshot]

[Features image][product-screenshot]


<p align="right">(<a href="#top">back to top</a>)</p>


### Built With

* [Pytorch](https://pytorch.org/)
* [scikit-learn](https://scikit-learn.org/)
* [Numpy](https://numpy.org/)
* [Pandas](https://pandas.pydata.org/)
* [Logging](https://docs.python.org/3/library/logging.html)
* [Seaborn](https://seaborn.pydata.org/)

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Getting Started

### Installation


First, clone the repository:
   ```sh
   git clone https://github.com/puchee99/TimeSeriesDL.git
   ```
Access to the project folder with:
  ```sh
  cd TimeSeriesDL
  ```

We will create a virtual environment with `python3`
* Create environment with python 3 
    ```sh
    python3 -m venv venv
    ```
    
* Enable the virtual environment
    ```sh
    source venv/bin/activate
    ```

* Install the python dependencies on the virtual environment
    ```sh
    pip install -r requirements.txt
    ```

<p align="right">(<a href="#top">back to top</a>)</p>

## Usage
The train.py and test.py documents can be executed with bash using different arguments.

* To get the information of the arguments use:
    ```sh
    python name_document.py -h
    ```
    Example:
    ```sh
    python train.py -h
    ```
* To train the models use:
    ```sh
    python train.py
    ```
* To test the models use:
    ```sh
    python test.py
    ```


## Roadmap

- [x] Test different models
- [ ] Train model as [PytorchClassifier](https://github.com/puchee99/PytorchClassifier)
- [ ] Loggers
- [ ] BI
    - [ ] Flask
    - [ ] Plotly

<p align="right">(<a href="#top">back to top</a>)</p>
<!-- CONTACT -->
## Contact

Arnau Puche  - [@arnau_puche_vila](https://www.linkedin.com/in/arnau-puche-vila-ds/) - arnaupuchevila@gmail.com

Project Link: [https://github.com/puchee99/JOBcn-DS-2022](https://github.com/puchee99/JOBcn-DS)


<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/puchee99/TimeSeriesDL2.svg?style=for-the-badge
[contributors-url]: https://github.com/puchee99/TimeSeriesDL/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/puchee99/TimeSeriesDL.svg?style=for-the-badge
[forks-url]: https://github.com/puchee99/TimeSeriesDL/network/members
[stars-shield]: https://img.shields.io/github/stars/puchee99/TimeSeriesDL.svg?style=for-the-badge
[stars-url]: https://github.com/puchee99/TimeSeriesDL/stargazers
[issues-shield]: https://img.shields.io/github/issues/puchee99/TimeSeriesDL.svg?style=for-the-badge
[issues-url]: https://github.com/puchee99/TimeSeriesDL/issues
[license-shield]: https://img.shields.io/github/license/puchee99/TimeSeriesDL.svg?style=for-the-badge
[license-url]: https://github.com/puchee99/TimeSeriesDL/blob/main/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/arnau-puche-vila-ds/

