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
  /* 1. LAYOUT FIX: Widen the page but keep TOC on the right */
  .page__inner-wrap {
    width: 85% !important;
    max-width: 1400px !important;
  }
  
  /* 2. COLOR FIX: Force Mint Green on all links */
  a { color: #158466 !important; }
  a:hover { color: #0b4f3c !important; text-decoration: underline; }
  .archive__item-title { color: #158466 !important; }

  /* 3. GRID LAYOUT: Authors | Title (No Year) */
  .pub-row {
    display: grid;
    /* Authors (30%) | Title (Auto) */
    grid-template-columns: 30% 1fr; 
    gap: 20px;
    align-items: baseline;
    padding: 10px 0;
    border-bottom: 1px solid #eee;
    font-size: 0.95em;
  }

  /* 4. Column Styling */
  .pub-authors {
    color: #555;
    white-space: normal; 
    word-wrap: break-word;
    line-height: 1.4;
  }

  .pub-title {
    color: #222;
    cursor: pointer;
    line-height: 1.4;
  }
  
  /* Hover effect */
  summary:hover .pub-title {
    color: #158466; 
    text-decoration: underline;
  }

  /* Mobile: Stack them */
  @media screen and (max-width: 800px) {
    .pub-row { grid-template-columns: 1fr; gap: 5px; }
    .pub-authors { font-size: 0.9em; color: #666; margin-bottom: 4px; }
  }
</style>

### Academic Positions

| Period | Position | Institution |
| :--- | :--- | :--- |
| 2022–Present | Associate Professor | Faculty of Mathematics, Natural Sciences and Information Technologies (University of Primorska) |
| 2016–2021 | Docent (Assistant Professor) | Faculty of Mathematics, Natural Sciences and Information Technologies (University of Primorska) |
| 2016–2018 | Postdoc (with Prof. R. Elsaesser) | Efficient Algorithms Group (Salzburg University) |
| 2015–2016 | Teaching Assistant | Faculty of Mathematics, Natural Sciences and Information Technologies (University of Primorska) |
| 2013 (Autumn)| Student Internship (with Prof. D. Kral) | Centre for Discrete Mathematics and its Applications (University of Warwick) |
| 2011–2015 | Teaching Assistant & PhD Student | Faculty of Mathematics and Physics (University of Ljubljana) |
| 2011–2015 | Young Researcher | Institute of Mathematics, Physics and Mechanics (Ljubljana) |

### Publications

{% assign publications = site.data.publications %}

{% for pub in publications %}
  <details>
    
    <summary style="list-style: none; outline: none; cursor: pointer;">
      <div class="pub-row">
        
        <div class="pub-authors" title="{{ pub.short_authors }}">
          {{ pub.short_authors | default: pub.author | replace: "M. Krnc", "•" | replace: "Matjaž Krnc", "•" }}
        </div>
        
        <div class="pub-title">{{ pub.title }}</div>
      </div>
    </summary>

    <div style="background: #f0fdf4; padding: 15px; margin-top: -1px; border-bottom: 1px solid #ccebd4; font-size: 0.9em;">
      
      <div style="margin-bottom: 10px; color: #444;">
        <strong>Year:</strong> {{ pub.year }} <br>
        
        {% if pub.journal %}
          <strong>Journal:</strong> <i>{{ pub.journal }}</i>
        {% elsif pub.booktitle %}
          <strong>Venue:</strong> <i>{{ pub.booktitle }}</i>
        {% endif %}
        <br>
        <strong>Full Authors:</strong> {{ pub.author | replace: " and ", ", " }}
      </div>

      <div>
        {% if pub.url %}
          <a href="{{ pub.url }}" style="text-decoration: none; padding: 4px 12px; background: #fff; color: #158466 !important; border: 1px solid #158466; border-radius: 4px; margin-right: 5px; font-size: 0.85em;">DOI / DBLP</a>
        {% endif %}
        
        {% if pub.arxiv_url %}
          <a href="{{ pub.arxiv_url }}" style="text-decoration: none; padding: 4px 12px; background: #fff; color: #158466 !important; border: 1px solid #158466; border-radius: 4px; margin-right: 5px; font-size: 0.85em;">arXiv</a>
        {% endif %}
        
        {% if pub.ee %}
           <a href="{{ pub.ee }}" style="text-decoration: none; padding: 4px 12px; background: #fff; color: #158466 !important; border: 1px solid #158466; border-radius: 4px; font-size: 0.85em;">PDF</a>
        {% endif %}
      </div>
      
    </div>
  </details>
{% endfor %}

<div style="margin-top: 30px; margin-bottom: 50px; font-size: 0.8em; color: #888;">
  Full lists available on <a href="./dblp_publications.html">DBLP</a> or <a href="https://bit.ly/Krnc-Scholar">Google Scholar</a>.
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

* **Europe:** INRIA (France), University of West Bohemia (Czech), Charles University (Czech), Pavol Jozef Šafárik University (Slovakia), Warsaw University (Poland), University of Zagreb (Croatia), LIAFA (France), Universität Hamburg (Germany), Cambridge (UK), Brandenburgische Technische Universität (Germany), Karl-Franzens-Universität Graz (Austria), Masaryk University (Czech).
* **USA:** Rhodes College (TN), University of Memphis (TN), Rutgers University (NJ).
* **Other:** HSE (Moscow), National Institute of Informatics (Tokyo).

### Organised Events

| Date | Event | Webpage |
| :--- | :--- | :--- |
| 2023 Oct. | SCORES 2023 - 9th Student Computing Research Symposium | [www.scores.si](https://www.scores.si/) |
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
Jernej Azarija, Vesna Andova, Nino Bašič, Gregor Bankhamer, Jesse Beisegel, Petra Berenbrink, Marthe Bonamy, Nina Chiarelli, Maria Chudnovsky, Clément Dallard, Andreas Darmann, Carolin Denkert, Zdenek Dvorak, Robert Elsaesser, Rok Erman, Robert Ganian, Frederik Garbe, Pascal Gollin, Eric Gottlieb, Janko Gravner, Vladimir Gurvich, Robert Hancock, Meike Hatzel, Frederic Havet, Claire Hilaire, Tomas Kaiser, Dominik Kaaser, Frantisek Kardos, Lukasz Kowalik, Peter Kling, Ekkehard Köhler, Daniel Kráľ, Martin Kupec, Ander Lamaison, Anita Liebenau, Borut Lužar, Aljoscha Mayer, Martin Milanič, Martina Mockovciakova, Samuel Mohr, Peter Muršič, Vít Musil, Sarka Petrickova, Ulrik Pferschy, Michał Pilipczuk, Tomaž Pisanski, Jean-Florent Raymond, Nicolás Rivera, Ondrej Rucky, Thomas Sauerwald, Joachim Schauer, Robert Scheffler, Jean-Sebastien Sereni, Ladislav Stacho, Martin Strehler, John Sylvester, Riste Škrekovski, Jan Volec, Misha Vyalyi, Tomasz Walen, Robin J Wilson, Zelealem Yilma.

### Thesis Supervision
Are you considering writing a thesis under my supervision? Please identify an area of math/CS you are passionate about, then email me to arrange a meeting.

### Useful Resources
- [Tips for Graduate Students](./graduate.html) - For those wishing to explore the world of mathematics.
- [The Hardy-Littlewood Collaboration Rule](./hardy-littlewood.html) - An overview of the collaboration ethos I support.