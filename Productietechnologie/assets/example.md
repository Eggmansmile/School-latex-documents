chapter{Voorbeeld Hoofdstuk}
In deze sectie tonen we hoe je formules en figuren toevoegt.

% Example formula entry (registers itself in the formularium)
\frm{Bernoulli}{p + \tfrac{1}{2}\rho v^2 + \rho g h = \text{constant}}{Energiebehoud langs een stroomlijn (incompressible, steady)}

% Placeholder figure drawn with TikZ (no external image required)
\begin{figure}[ht]
  \centering
  \begin{tikzpicture}
    \draw[gray,thick] (0,0) rectangle (10,4);
    \node at (5,2) {Plaatsaanduiding: vervang met \texttt{assets/<naam>.png} en gebruik \textbackslash fig{} in future};
  \end{tikzpicture}
  \caption{Voorbeeld plaatshouder}
  \label{fig:placeholder}
\end{figure}

\section{Formules kort}
De belangrijkste formules die in de tekst gebruikt zijn, worden verzameld onderaan in het formularium.

\begin{formularium}
% entries are appended automatically by \frm commands throughout the document
\end{formularium}

\chapter{Afbeeldingen}
Plaats afbeeldingen in `Productietechnologie/assets/` en voeg ze in met het hulpcommando:

\begin{verbatim}
\fig[0.7\linewidth]{Productietechnologie/assets/voorbeeld.png}{Bijschrift}{fig:voorbeeld}
\end{verbatim}

% --- Add more chapters below as needed ---
