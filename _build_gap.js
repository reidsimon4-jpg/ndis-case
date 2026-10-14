const fs = require("fs");
const {
  Document, Packer, Paragraph, TextRun, AlignmentType, LevelFormat,
  HeadingLevel, Header, Footer, PageNumber, BorderStyle
} = require("docx");

const P = (children, opts = {}) => new Paragraph({ children, spacing: { after: 160, line: 276 }, ...opts });
const T = (text, opts = {}) => new TextRun({ text, font: "Arial", ...opts });
const H = (text, lvl = HeadingLevel.HEADING_2) => new Paragraph({ heading: lvl, children: [new TextRun(text)] });
const relief = (text) => new Paragraph({ numbering: { reference: "relief", level: 0 }, spacing: { after: 140, line: 276 }, children: [T(text)] });
const issue = (lead, text) => new Paragraph({ numbering: { reference: "issues", level: 0 }, spacing: { after: 140, line: 276 }, children: [T(lead, { bold: true }), T(text)] });
const circ = (text) => new Paragraph({ numbering: { reference: "circ", level: 0 }, spacing: { after: 140, line: 276 }, children: [T(text)] });
const order = (text) => new Paragraph({ numbering: { reference: "orders", level: 0 }, spacing: { after: 140, line: 276 }, children: [T(text)] });
const rule = () => new Paragraph({ spacing: { after: 160 }, border: { bottom: { style: BorderStyle.SINGLE, size: 6, color: "888888", space: 1 } }, children: [T("")] });

const doc = new Document({
  styles: {
    default: { document: { run: { font: "Arial", size: 22 } } },
    paragraphStyles: [
      { id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 26, bold: true, font: "Arial" }, paragraph: { spacing: { before: 240, after: 160 }, outlineLevel: 0 } },
      { id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 23, bold: true, font: "Arial" }, paragraph: { spacing: { before: 220, after: 120 }, outlineLevel: 1 } },
    ]
  },
  numbering: {
    config: [
      { reference: "relief", levels: [{ level: 0, format: LevelFormat.DECIMAL, text: "%1.", alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 600, hanging: 360 } } } }] },
      { reference: "issues", levels: [{ level: 0, format: LevelFormat.LOWER_LETTER, text: "(%1)", alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 600, hanging: 360 } } } }] },
      { reference: "circ", levels: [{ level: 0, format: LevelFormat.LOWER_LETTER, text: "(%1)", alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 600, hanging: 360 } } } }] },
      { reference: "orders", levels: [{ level: 0, format: LevelFormat.DECIMAL, text: "%1.", alignment: AlignmentType.LEFT, style: { paragraph: { indent: { left: 600, hanging: 360 } } } }] },
    ]
  },
  sections: [{
    properties: { page: { size: { width: 12240, height: 15840 }, margin: { top: 1440, right: 1440, bottom: 1440, left: 1440 } } },
    headers: { default: new Header({ children: [ new Paragraph({ alignment: AlignmentType.RIGHT, spacing: { after: 0 }, children: [ new TextRun({ text: "DRAFT — verify lodgement form (GAP Practice Direction 2026) before filing", font: "Arial", size: 16, color: "AA0000", italics: true }) ] }) ] }) },
    footers: { default: new Footer({ children: [ new Paragraph({ alignment: AlignmentType.CENTER, children: [ new TextRun({ text: "Page ", font: "Arial", size: 18 }), new TextRun({ children: [PageNumber.CURRENT], font: "Arial", size: 18 }), new TextRun({ text: " of ", font: "Arial", size: 18 }), new TextRun({ children: [PageNumber.TOTAL_PAGES], font: "Arial", size: 18 }) ] }) ] }) },
    children: [
      new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 40 }, children: [T("ADMINISTRATIVE REVIEW TRIBUNAL", { bold: true, size: 26 })] }),
      new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 160 }, children: [T("BRISBANE REGISTRY", { bold: true, size: 22 })] }),
      new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 20 }, children: [T("No. 2023/3361  —  Vida REID and Commissioner of the NDIS Quality and Safeguards Commission")] }),
      new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 20 }, children: [T("No. 2023/3363  —  Simon REID and Commissioner of the NDIS Quality and Safeguards Commission")] }),
      new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 160 }, children: [T("No. 2023/4494  —  Forward Focused Group Pty Ltd and Commissioner of the NDIS Quality and Safeguards Commission")] }),
      rule(),
      new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 40 }, children: [T("APPLICANTS’ REQUEST THAT THE PRESIDENT REFER THE APPLICATIONS TO THE", { bold: true, size: 24 })] }),
      new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 40 }, children: [T("GUIDANCE AND APPEALS PANEL (s 122) AND, IN THE ALTERNATIVE,", { bold: true, size: 24 })] }),
      new Paragraph({ alignment: AlignmentType.CENTER, spacing: { after: 160 }, children: [T("FOR AN EXPEDITED CONSOLIDATED HEARING", { bold: true, size: 24 })] }),
      rule(),
      new Paragraph({ spacing: { after: 60 }, children: [ T("To:  ", { bold: true }), T("The Honourable Justice Emilios Kyrou AO, President, Administrative Review Tribunal (via the Brisbane Registry).") ] }),
      new Paragraph({ spacing: { after: 60 }, children: [ T("From:  ", { bold: true }), T("Simon Reid (applicant in No. 2023/3363, and as a director of Forward Focused Group Pty Ltd in No. 2023/4494) and Vida Reid (applicant in No. 2023/3361).") ] }),
      new Paragraph({ spacing: { after: 200 }, children: [ T("Date:  ", { bold: true }), T("13 June 2026") ] }),

      H("A.  What is sought"),
      P([T("The applicants respectfully invite the President to exercise the power in section 122 of the Administrative Review Tribunal Act 2024 (Cth) (the Act) and request the following:")]),
      relief("That the President, on his own initiative, refer the three above applications (together with any related application of the applicants before the Tribunal) to the Guidance and Appeals Panel, on the ground that they raise an issue of significance to administrative decision-making and that it is in the interests of justice that the Tribunal be so constituted (s 122(1)(b)); and"),
      relief("That the applications, once referred, be listed for a single, expedited final hearing on the common factual substratum they share."),
      P([T("In the alternative, if the President is not minded to refer the applications, the applicants request that the matters be listed together for an expedited final hearing in the ordinary division, in accordance with the Tribunal’s objective in section 9 and the directions power in section 79 of the Act.")]),

      H("B.  The matters and the parties"),
      P([T("Each application is an application for review of a banning order made by the Commissioner of the NDIS Quality and Safeguards Commission (the Commission) on 21 December 2022, and of the related internal review decisions made in 2023. The three applications have been case-managed together throughout, most recently under directions made by Deputy President K McMillan KC on 8 September 2025, and are listed together in the respondent’s correspondence. They turn on a single, common body of facts.")]),

      H("C.  The delay, and a banning order that has expired before any hearing on the merits"),
      P([T("The applications have been on foot since 2023. No final hearing on the merits has yet taken place. In the meantime the sanctions under review have continued to run, and one has now run its entire course:")]),
      P([ T("The banning order against Forward Focused Group Pty Ltd has "), T("already expired.", { bold: true }), T(" The respondent has confirmed in writing, by letter from the Australian Government Solicitor dated 13 February 2026 (ref. 23001627), that the order against FFG “expired at 6pm on 20 December 2025 and is no longer in force”, and that the Commission’s public register has been updated to record that expiry.") ]),
      P([ T("In the same letter, the respondent "), T("invited FFG to consider withdrawing its application", { italics: true }), T(" “given the banning order against FFG has expired”. The practical effect is that the time taken to bring the matter to hearing has consumed the whole of the sanction — and the respondent now relies on that very fact to suggest the review need not proceed. A right of review that is overtaken by the expiry of the order it challenges is, in substance, no review at all.") ]),
      P([ T("The applicants’ individual five-year banning orders, also made on 21 December 2022, are due to expire in December 2027. On the present trajectory they too may approach or reach expiry before a merits hearing. The applicants do not accept that expiry renders any matter moot: the orders remain published on the Commission’s register indefinitely (as the respondent’s letter acknowledges); the revocation of FFG’s registration is a separate and continuing consequence; and the findings underpinning the orders bear directly on the applicants’ reputations and livelihoods and on the related matters.") ]),
      P([T("This is the central reason the applicants seek referral and expedition: section 9 of the Act requires that applications be resolved “as quickly … as a proper consideration of the matters before the Tribunal permits”. The integrity of that guarantee is engaged where a reviewable sanction expires unheard.")]),

      H("D.  The power: section 122"),
      P([T("Section 122(1) provides that where an application for review is made to the Tribunal, the President may refer the application to the Guidance and Appeals Panel if the President is satisfied that:")]),
      P([ T("(i) the application raises an "), T("issue of significance to administrative decision-making", { bold: true }), T("; and") ], { indent: { left: 360 } }),
      P([ T("(ii) it is "), T("appropriate in the interests of justice", { bold: true }), T(" that the Tribunal be constituted by the Guidance and Appeals Panel for the purposes of the proceeding.") ], { indent: { left: 360 } }),
      P([T("Section 122(2) requires that, for the second limb, the President must have regard to the circumstances of the parties to the proceeding. On a referral, the Tribunal is constituted by the Guidance and Appeals Panel under section 40. The applicants address each limb below.")]),

      H("E.  Limb one — issue of significance to administrative decision-making"),
      P([T("The applications raise the following issues, each of which has significance beyond the applicants’ own matters:")]),
      issue("Reviews defeated by delay.  ", "Whether, and how, the Tribunal should manage the review of time-limited regulatory sanctions so that the right of review conferred by the legislation is not rendered nugatory by the expiry of the sanction during the proceeding. The FFG order — which expired on 20 December 2025 before any merits hearing — is a live exemplar. The Commission issues many time-limited banning orders, and the question of how the review system protects against delay-induced mootness is plainly significant to administrative decision-making generally."),
      issue("The standard for a “suitability” banning order.  ", "The proper approach to banning orders made on the “suitability” ground under s 73ZN(2)(a)(iii) of the National Disability Insurance Scheme Act 2013 (Cth), including whether and to what extent an individual’s suitability may be assessed by attributing to that individual the conduct of corporate entities, or of other persons, without an individualised assessment of the individual’s own conduct and knowledge. There is no published Tribunal decision setting aside such an order; authoritative guidance would assist a class of decisions."),
      issue("Variation of the statutory basis without notice.  ", "The requirements of procedural fairness where an internal reviewer varies the statutory foundation of a banning order — here, from the contravention limb to the suitability limb — without giving the affected person notice that the new basis is the dispositive issue and an opportunity to address it (the principle in SZBEL v Minister for Immigration and Multicultural and Indigenous Affairs (2006) 228 CLR 152 and Kioa v West (1985) 159 CLR 550). This recurs across regulatory internal review and is of general importance."),
      issue("Adequacy of service of notices of intention.  ", "The procedural-fairness consequences where a notice of intention is served late, after the response deadline, and on a person other than the named recipient or the solicitors of record."),
      P([T("The applicants note that issue (a) in particular is one on which a determination by the Guidance and Appeals Panel would provide guidance of real practical value to the Tribunal, to the Commission and to participants in the scheme.")]),

      H("F.  Limb two — interests of justice and the circumstances of the parties (s 122(2))"),
      P([T("It is in the interests of justice that these applications be heard by the Guidance and Appeals Panel, having regard to the circumstances of the parties:")]),
      circ("The applications have been unresolved since 2023, and one of the reviewable sanctions has already expired in full without a hearing. The delay is itself the principal injustice the applicants face."),
      circ("The applicants are self-represented individuals and a small family company. They have nonetheless engaged consistently with the Tribunal’s processes and with repeated interlocutory steps, including the respondent’s pending application under section 70 of the Act to restrict disclosure of material."),
      circ("The three matters share a single factual substratum and are already managed together. A single, senior constitution determining them together would avoid inconsistent findings, reduce the piecemeal interlocutory skirmishing that has characterised the matters to date, and bring the proceedings to a just and final conclusion."),
      circ("The matters arise in the context of coordinated, multi-agency regulatory action. The applicants contend that the conduct affecting them spanned a number of Commonwealth agencies acting in concert. A single authoritative determination is the appropriate way to resolve matters of that character."),
      circ("The respondent’s response to the delay has been to invite withdrawal of the FFG application on the basis of expiry. Referral and expedition is the just alternative: it ensures the merits are determined rather than defeated by the passage of time."),

      H("G.  Why the Guidance and Appeals Panel, and the alternative"),
      P([T("Referral to the Guidance and Appeals Panel is appropriate because the matters combine issues of general significance with circumstances that make a prompt, authoritative and final determination important to the parties. A more senior constitution is well suited to resolving the common questions across all three matters in one hearing.")]),
      P([T("If, however, the President is not satisfied that referral is warranted, the applicants respectfully ask that the same considerations of delay and fairness be addressed by listing the three matters together for an expedited final hearing in the ordinary division, with a timetable fixed for any remaining steps, consistent with sections 9 and 79 of the Act.")]),

      H("H.  Orders sought"),
      order("That the President refer applications No. 2023/3361, No. 2023/3363 and No. 2023/4494 (and any related application) to the Guidance and Appeals Panel under section 122 of the Act."),
      order("That the referred applications be listed for a single expedited final hearing on the common issues."),
      order("In the alternative, that the three applications be listed together for an expedited final hearing in the ordinary division, with directions fixing the date for hearing and the steps to be taken beforehand."),
      order("Such further or other direction as the Tribunal considers appropriate to ensure the applications are resolved as quickly as a proper consideration of the matters permits."),

      new Paragraph({ spacing: { before: 320, after: 40 }, children: [T("Dated: 13 June 2026")] }),
      new Paragraph({ spacing: { before: 240, after: 0 }, children: [T("__________________________")] }),
      new Paragraph({ spacing: { after: 200 }, children: [T("Simon Reid", { bold: true }), T("  — applicant in person (No. 2023/3363); and as a director of Forward Focused Group Pty Ltd (No. 2023/4494)")] }),
      new Paragraph({ spacing: { before: 120, after: 0 }, children: [T("__________________________")] }),
      new Paragraph({ spacing: { after: 200 }, children: [T("Vida Reid", { bold: true }), T("  — applicant in person (No. 2023/3361)")] }),

      rule(),
      new Paragraph({ spacing: { before: 80, after: 40 }, children: [T("Notes for review before filing (delete this section before lodging)", { bold: true, italics: true, size: 18, color: "AA0000" })] }),
      new Paragraph({ spacing: { after: 60 }, children: [T("1. Confirm the correct lodgement channel and form for inviting a s 122 referral against the Guidance and Appeals Panel Practice Direction 2026 (commenced 2 March 2026); a first-instance referral under s 122 is the President’s own-initiative power, so this is framed as an invitation, not an application of right.", { size: 18, italics: true })] }),
      new Paragraph({ spacing: { after: 60 }, children: [T("2. Re-verify every statutory and case citation against a primary source immediately before filing, consistent with the standing rule of the matter. The case citations used (SZBEL; Kioa) are on the matter’s verified-authorities list; the ART Act sections (9, 40, 70, 79, 122) were verified against the Federal Register of Legislation / AustLII.", { size: 18, italics: true })] }),
      new Paragraph({ spacing: { after: 60 }, children: [T("3. Confirm the present procedural posture (e.g., the outcome of the 20 March 2026 interlocutory hearing and the status of the s 70 application) and update Parts B, C and F accordingly.", { size: 18, italics: true })] }),
      new Paragraph({ spacing: { after: 60 }, children: [T("4. Confirm Vida Reid joins as a signatory, or adjust the From / signature blocks accordingly.", { size: 18, italics: true })] }),
    ]
  }]
});

Packer.toBuffer(doc).then(buf => { fs.writeFileSync("/sessions/optimistic-epic-curie/mnt/NDIS Case/GAP_Referral_Request_DRAFT_13_June_2026.docx", buf); console.log("WROTE", buf.length); });
