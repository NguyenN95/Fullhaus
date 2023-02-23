<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
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
  <a href="https://github.com/NguyenN95/Fullhaus">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">Fullhaus Test</h3>

  <p align="center">
    Fullhaus test
    <br />
    <a href="https://github.com/NguyenN95/Fullhaus#readme"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/NguyenN95/Fullhaus">View Demo</a>
    ·
    <a href="https://github.com/NguyenN95/Fullhaus/issues">Report Bug</a>
    ·
    <a href="https://github.com/NguyenN95/Fullhaus/issues">Request Feature</a>
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
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#help">Help</a></li>
    <li><a href="#checklist">Checklist</a></li>
    <li><a href="#version-history">Version history</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

Build a classification model classify (an) image(s) into 3 categories (Bed, Sofa, Chair), apply that to an API server (Fastapi)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![FastAPI][FastAPI]][FastAPI-url]
* [![Docker][Docker]][Docker-url]
* [![Tensorflow][Tensorflow]][Tensorflow-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

Download [python 3.10 or greater][Python-url]

Download [Docker][Docker-url] (**Optional**)

### Installation

1. Clone the repo
   ```bash
   git clone https://github.com/NguyenN95/Fullhaus.git
   ```
2. Create virtual environment (**None Docker version**)
   * Linux 
      ```bash
      python3 -m venv env
      ```
   * Windows 
      ```powershell
      python -m venv env
      ```
3. Activate virtual environment (**None Docker version**)
   * Linux 
      ```bash
      source ./env/Scripts/activate
      ```
   * Windows 
      ```powershell
      .\env\Scripts\activate.ps1
      ```
4. Install libraries (**None Docker version**)
   * Linux 
      ```bash
      pip3 install -r requirements.txt
      ```
   * Windows 
      ```powershell
      pip install -r requirements.txt
      ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

1. Local Server
   * Deploy local server
      * Docker environment
      ```bash
      docker-compose up -d
      ```
      * Host environment
      ```bash
      cd ./src
      uvicorn main:app --reload
      ```
   * Open web browser and type http://localhost:8000/docs to open Swagger UI 
   * Upload an image via `/predicts-image`
2. Test
   * Before running test make sure these dependencies installed
   ```bash
   pip install pytest httpx
   ```
   * Run
   ```bash
   cd ./src
   pytest
   ```

_For more examples, please refer to the [Docker docs](https://docs.docker.com/), [Tensorflow docs](https://www.tensorflow.org/api_docs/python/tf), [Fastapi](https://fastapi.tiangolo.com/), [Github actions](https://docs.github.com/en/actions)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- HELP -->
## Help

Any advise for common problems or issues.
* Docker
  ```bash
  docker --help
  ```

* Python
  ```bash
  python --help
  ```

* Pip
  ```bash
  pip --help
  ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Checklist

- [x] Build a classification model
- [x] Build an API to access the model
- [x] Create a Docker image of your code by following docker best practices
- [x] Implement CI/CD pipeline on Github Actions
- [x] Add a clear README file with instructions.

See the [open issues](https://github.com/NguyenN95/Fullhaus/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- Version history -->
## Version History

* 0.1
    * Initial Release

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Nguyen - [@Nguyen Linkedin](https://www.linkedin.com/in/binhnguyennguyen/)

Project Link: [https://github.com/NguyenN95/Fullhaus](https://github.com/NguyenN95/Fullhaus)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Best-README-Template](https://github.com/othneildrew/Best-README-Template)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

<!-- How to make badages Reference -->
<!-- https://github.com/Ileriayo/markdown-badges -->
<!-- https://javascript.plainenglish.io/how-to-make-custom-language-badges-for-your-profile-using-shields-io-d2aeaf016b6b -->

[contributors-shield]: https://img.shields.io/github/contributors/NguyenN95/Fullhaus.svg?style=for-the-badge
[contributors-url]: https://github.com/NguyenN95/Fullhaus/graphs/contributors

[forks-shield]: https://img.shields.io/github/forks/NguyenN95/Fullhaus.svg?style=for-the-badge
[forks-url]: https://github.com/NguyenN95/Fullhaus/network/members

[stars-shield]: https://img.shields.io/github/stars/NguyenN95/Fullhaus.svg?style=for-the-badge
[stars-url]: https://github.com/NguyenN95/Fullhaus/stargazers

[issues-shield]: https://img.shields.io/github/issues/NguyenN95/Fullhaus.svg?style=for-the-badge
[issues-url]: https://github.com/NguyenN95/Fullhaus/issues

[license-shield]: https://img.shields.io/github/license/NguyenN95/Fullhaus.svg?style=for-the-badge
[license-url]: https://github.com/NguyenN95/Fullhaus/blob/master/LICENSE.txt

[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/nguyenn95/

[TensorFlow]: https://img.shields.io/badge/TensorFlow-%23FF6F00.svg?style=for-the-badge&logo=TensorFlow&logoColor=white
[TensorFlow-url]: https://www.tensorflow.org/

[Docker]: https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white
[Docker-url]: https://www.docker.com/

[FastAPI]: https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi
[FastAPI-url]: https://fastapi.tiangolo.com/