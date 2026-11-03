---
layout: single
author_profile: true
permalink: /
title: "Curriculum Vitae"
toc: true
toc_sticky: true
toc_label: "Jump to"
toc_icon: "list"
---

### Research Interests
- Structural and algorithmic graph theory
- Extremal graph theory, combinatorial limits
- Combinatorial game theory
- Population protocols, distributed consensus

<style>
  .site-title { display: none !important; }

  .page__inner-wrap {
    width: 85% !important;
    max-width: 1400px !important;
  }

  .publications {
    font-size: 0.8em;
  }

  .publication-header,
  .publication-summary {
    display: grid;
    grid-template-columns: 35% 1fr;
    gap: 15px;
    align-items: baseline;
    padding: 6px 8px;
    border-bottom: 1px solid #e2e2e2;
    line-height: 1.4;
  }

  .publication-header {
    border-bottom: 2px solid #555;
    color: #333;
    font-weight: bold;
  }

  .publication-authors {
    color: #555;
    word-wrap: break-word;
  }

  .publication-title {
    color: #222;
  }

  .publication > summary {
    cursor: pointer;
    list-style: none;
  }

  .publication > summary::-webkit-details-marker {
    display: none;
  }

  .publication > summary:hover .publication-title,
  .publication > summary:focus-visible .publication-title {
    text-decoration: underline;
  }

  .publication-details {
    background: #fcfcfc;
    margin-bottom: 10px;
    padding: 10px 15px;
    border-bottom: 1px solid #e2e2e2;
  }

  .publication-citation {
    color: #444;
    margin: 0 0 8px;
  }

  .publication-links a + a::before {
    content: " · ";
    color: #777;
  }

  .publication-more {
    color: #888;
    margin: 20px 0 50px;
  }

  @media screen and (max-width: 800px) {
    .publication-header { display: none; }
    .publication-summary { grid-template-columns: 1fr; gap: 4px; }
    .publication-authors { font-weight: bold; }
  }
</style>

### Academic Positions

| Period | Position | Institution |
| :--- | :--- | :--- |
| 2026–Present | Chair of KSPV Catedra | UP FTPO |
| 2022–Present | Associate Professor | UP FAMNIT, UP FTPO, UNM FIŠ |
| 2016–2021 | Docent (Assistant Professor) | Faculty of Mathematics, Natural Sciences and Information Technologies (University of Primorska) |
| 2016–2018 | Postdoc (with Prof. R. Elsaesser) | Efficient Algorithms Group (Salzburg University) |
| 2015–2016 | Teaching Assistant | Faculty of Mathematics, Natural Sciences and Information Technologies (University of Primorska) |
| 2013 (Autumn)| Student Internship (with Prof. D. Kral) | Centre for Discrete Mathematics and its Applications (University of Warwick) |
| 2011–2015 | Teaching Assistant & PhD Student | Faculty of Mathematics and Physics (University of Ljubljana) |
| 2011–2015 | Young Researcher | Institute of Mathematics, Physics and Mechanics (Ljubljana) |

### Publications

{% assign publications = site.data.publications %}

<div class="publications">
  <div class="publication-header" aria-hidden="true">
    <div>Authors</div>
    <div>Title</div>
  </div>

  {% for pub in publications %}
    <details class="publication">
      <summary class="publication-summary">
        <span class="publication-authors" title="{{ pub.short_authors }}">
          {{ pub.short_authors | default: pub.author | replace: "M. Krnc", "•" | replace: "Matjaž Krnc", "•" }}
        </span>
        <span class="publication-title">{{ pub.title }}</span>
      </summary>

      <div class="publication-details">
        <p class="publication-citation">
          <strong>Year:</strong> {{ pub.year }} &nbsp;|&nbsp;
          {% if pub.journal %}
            <strong>Journal:</strong> <i>{{ pub.journal }}</i>
          {% elsif pub.booktitle %}
            <strong>Venue:</strong> <i>{{ pub.booktitle }}</i>
          {% endif %}
          <br>
          <strong>Full Authors:</strong> {{ pub.author | replace: " and ", ", " }}
        </p>

        <div class="publication-links">
          {% if pub.url %}
            <a href="{{ pub.url }}">DOI / DBLP</a>
          {% endif %}

          {% if pub.arxiv_url %}
            <a href="{{ pub.arxiv_url }}">arXiv</a>
          {% endif %}

          {% if pub.ee %}
            <a href="{{ pub.ee }}">PDF</a>
          {% endif %}
        </div>
      </div>
    </details>
  {% endfor %}

  <p class="publication-more">
    Full lists available on <a href="./dblp_publications.html">DBLP</a> or <a href="https://bit.ly/Krnc-Scholar">Google Scholar</a>.
  </p>
</div>

### Grants & Awards

| Year | Details |
| :--- | :--- |
| 2022–2024 | ARRS bilateral research project (BI-US/22-24-093), with Rutgers University (USA) |
| 2019–2021 | ARRS bilateral research project (BI-US/19-21-018), with Rutgers University (USA) |
| 2019 | Erasmus+ mobility project with Brandenburg University of Technology Cottbus–Senftenberg |
| 2016 | Funds for attending São Paulo School of Advanced Science on Algorithms, Combinatorics and Optimization |
| 2015 | Award for early PhD defense |
| 2013 | Ad-futura mobility grant for PhD students (Research visit to Warwick University) |

### Talks & Visits

**Seminar Talks & Public Lectures**

| Date | Institution |
| :--- | :--- |
| 2026 May | Matematika je kul (Summer school for mathematics, UP FAMNIT) |
| 2026 Mar. | Monday with Murthay seminar, University of Haifa, Israel |
| 2025 Nov. | Rhodes College, Tennessee, USA |
| 2025 Sep. | DIGI-MAT: Workshop on Teaching Mathematics using Digital Tools (Cryptography) |
| 2025 Apr. | FAMNIT math seminar |
| 2024 May | Fachgebiet Diskrete Mathematik und Grundlagen der Informatik (B-TU Cottbus) |
| 2024 Feb. | Rhodes College, Tennessee, USA |
| 2024 Feb. | Institute of Combinatorics, University of Memphis, USA |
| 2023 Mar. | Masaryk University, Brno, Czech Republic |
| 2023 Mar. | Fachgebiet Diskrete Mathematik und Grundlagen der Informatik (B-TU Cottbus) |
| 2022 Aug. | ORADA (Computer Science Summer School at UP FAMNIT) |
| 2020 Mar. | Masaryk University, Brno, Czech Republic |
| 2020 Feb. | Fachgebiet Diskrete Mathematik und Grundlagen der Informatik (B-TU Cottbus) |
| 2019 Nov. | Open University, Milton Keynes, UK |
| 2019 Aug. | HSE, Faculty of Computer Science, Moscow |
| 2019 May | FIN-TECH Risk management workshop on Blockchains (Joseph Stefan Institute) |
| 2019 Jan. | Matematični dan (Public Lecture, UP FAMNIT) |
| 2018 Dec. | Department of Mathematics, FAMNIT (UP) |
| 2018 Aug. | Matematika je kul (Summer school for mathematics, UP FAMNIT) |
| 2018 Feb. | Software Tools for Mathematics, SageDays'97 workshop (UP FAMNIT) |
| 2018 Feb. | Fachgebiet Diskrete Mathematik und Grundlagen der Informatik (B-TU Cottbus) |
| 2017 Nov. | Computer Laboratory (University of Cambridge) |
| 2017 Oct. | Oberseminar Arbeitsbereich ART, Fachbereich Informatik (Universität Hamburg) |
| 2016 Jun. | Efficient Algorithms Group (Salzburg University) |
| 2016 Apr. | Department of Information Science and Technologies, FAMNIT (UP) |

**Research Visits**

* **Europe:** INRIA (France), University of West Bohemia (Czech), Charles University (Czech), Pavol Jozef Šafárik University (Slovakia), Warsaw University (Poland), University of Zagreb (Croatia), LIAFA (France), Universität Hamburg (Germany), Cambridge University (UK), Brandenburgische Technische Universität (Germany), Karl-Franzens-Universität Graz (Austria), Masaryk University (Czech).
* **USA:** Princeton University (NJ), Rutgers University (NJ), Rhodes College (TN), University of Memphis (TN).
* **Other:** HSE (Moscow), National Institute of Informatics (Tokyo).

### Organised Events

| Date | Event | Link |
| :--- | :--- | :--- |
| 2026 Oct. | SCORES 2026 - 12th Student Computing Research Symposium | [www.scores.si](https://www.scores.si/) |
| 2026 Avg. | SCORES 2026 - 12th Student Computing Research Symposium | [www.scores.si](https://www.scores.si/) 
| 2025 Avg. | SGTAC 2026 - Structural Graph Theory Workshop on the Adriatic Coast | [sgtac.famnit.upr.si/](https://sgtac.famnit.upr.si/) |
| 2024 Jun. | WG 2024 - 50th International Workshop on Graph-Theoretic Concepts in Computer Science | [conferences.famnit.upr.si/event/31/](https://conferences.famnit.upr.si/event/31/) |
| 2023 Oct. | SCORES 2023 - 9th Student Computing Research Symposium | [www.scores.si](https://www.scores.si/) |
| 2023 Apr. | Brno-Koper Graph Theory Workshop (Gozd Martuljek, Kranjska Gora, Slovenia) |  |
| 2022 Oct. | MATCOS 2022 : Middle-European Conference on Applied Theoretical Computer Science | [matcos.iam.upr.si](http://matcos.iam.upr.si) |
| 2021 Sep. | GROW 2022 : The Workshop on Graph Classes, Optimization and Width Parameters | [grow.famnit.upr.si](http://grow2021.famnit.upr.si) |
| 2019 Oct. | MATCOS 2019 : Middle-European Conference on Applied Theoretical Computer Science | [matcos.iam.upr.si](http://matcos.iam.upr.si) |
| 2019 Oct. | StuCoSReC 2019 - The 6th Student Computer Science Research Conference | [stucosrec.feri.um.si/2019](http://stucosrec.feri.um.si/2019) |
| 2018 Feb. | Software Tools for Mathematics, SageDays'97 workshop | [stm.famnit.upr.si](http://stm.famnit.upr.si) |

### Research Collaborations & Students

**MSc Students:**
Mikita Akulich, Nina Klobas, Nevena Pivač, Ina Bašić.

**BSc Students:**
Mikita Akulich, Jelena Ilić, Đorđe Klisura, Ina Bašić, Hannah Meit.

**Research Collaborators:**
I have had the pleasure of doing research (one week or more) with:
Jernej Azarija, Vesna Andova, Nino Bašič, Gregor Bankhamer, Jesse Beisegel, Petra Berenbrink, Marthe Bonamy, Nina Chiarelli, Maria Chudnovsky, Julien Codsi, Clément Dallard, Andreas Darmann, Carolin Denkert, Zdenek Dvorak, Robert Elsaesser, Rok Erman, Robert Ganian, Frederik Garbe, Pascal Gollin, Eric Gottlieb, Janko Gravner, Vladimir Gurvich, Robert Hancock, Meike Hatzel, Frederic Havet, Claire Hilaire, Tomas Kaiser, Dominik Kaaser, Frantisek Kardos, Lukasz Kowalik, Peter Kling, Ekkehard Köhler, Daniel Kráľ, Martin Kupec, Ander Lamaison, Anita Liebenau, Borut Lužar, Aljoscha Mayer, Martin Milanič, Martina Mockovciakova, Samuel Mohr, Peter Muršič, Vít Musil, Sarka Petrickova, Ulrik Pferschy, Michał Pilipczuk, Tomaž Pisanski, Jean-Florent Raymond, Nicolás Rivera, Ondrej Rucky, Thomas Sauerwald, Joachim Schauer, Robert Scheffler, Jean-Sebastien Sereni, Ladislav Stacho, Martin Strehler, John Sylvester, Riste Škrekovski, Jan Volec, Misha Vyalyi, Tomasz Walen, Robin J Wilson, Zelealem Yilma.

### Thesis Supervision
Are you considering writing a thesis under my supervision? Please identify an area of math/CS you are passionate about, then email me to arrange a meeting.
Alternatively, take a look at our [GRASP page](https://grasp.famnit.upr.si). 

### Useful Resources
From Fan Chung's webpage. 
- [Tips for Graduate Students](./graduate.html) - For those wishing to explore the world of mathematics.
- [The Hardy-Littlewood Collaboration Rule](./hardy-littlewood.html) - An overview of the collaboration ethos I support.
