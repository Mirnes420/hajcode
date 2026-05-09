import streamlit as st

# Translations Dictionary
t = {
    "title": {"EN": "HAJ CODE Project Estimator & Proposal Generator", "BS": "HAJ CODE Procjenitelj Projekata i Generator Ponuda"},
    "intro": {"EN": "Input client requirements to generate a preliminary project scope, estimates, and relevant portfolio examples.", "BS": "Unesite zahtjeve klijenta kako biste generisali preliminarni obim projekta, procjene i relevantne primjere iz portfolija."},
    "client_details": {"EN": "Client Project Details", "BS": "Detalji Projekta Klijenta"},
    "client_name": {"EN": "Client Name", "BS": "Ime Klijenta"},
    "project_name": {"EN": "Project Name/Brief Title", "BS": "Ime Projekta/Kratki Naslov"},
    "project_type": {"EN": "Project Type", "BS": "Vrsta Projekta"},
    "features": {"EN": "Key Features/Modules (Select all that apply)", "BS": "Ključne Funkcionalnosti/Moduli (Odaberite sve primjenjivo)"},
    "desc": {"EN": "Detailed Requirements/Project Description", "BS": "Detaljni Zahtjevi/Opis Projekta"},
    "desc_placeholder": {"EN": "Describe the project vision, core functionalities, and any specific technologies or integrations needed.", "BS": "Opišite viziju projekta, osnovne funkcionalnosti i sve specifične tehnologije ili integracije koje su potrebne."},
    "timeline": {"EN": "Desired Timeline (Weeks)", "BS": "Željeni Vremenski Okvir (Sedmice)"},
    "budget": {"EN": "Approximate Budget Range (€)", "BS": "Približni Raspon Budžeta (€)"},
    "btn_generate": {"EN": "Generate Proposal", "BS": "Generiši Ponudu"},
    "err_client": {"EN": "Please enter a Client Name.", "BS": "Molimo unesite Ime Klijenta."},
    "err_project": {"EN": "Please enter a Project Name/Brief Title.", "BS": "Molimo unesite Ime Projekta/Kratki Naslov."},
    "analyzing": {"EN": "Analyzing requirements and generating proposal...", "BS": "Analiziranje zahtjeva i generisanje ponude..."},
    "overview_for": {"EN": "Generated Project Overview for", "BS": "Generisani Pregled Projekta za"},
    "scope_title": {"EN": "Proposed Project Scope & Tech Stack", "BS": "Predloženi Obim Projekta i Tehnologije"},
    "time_cost_title": {"EN": "Estimated Time & Cost", "BS": "Procijenjeno Vrijeme i Trošak"},
    "preliminary_desc": {"EN": "*This is a preliminary estimate and subject to detailed discovery.*", "BS": "*Ovo je preliminarna procjena i podložna je detaljnoj analizi.*"},
    "portfolio_title": {"EN": "Relevant HAJ CODE Portfolio Examples", "BS": "Relevantni Primjeri HAJ CODE Portfolija"},
    "why_title": {"EN": "Why Choose HAJ CODE d.o.o.?", "BS": "Zašto Odabrati HAJ CODE d.o.o.?"},
    "btn_download": {"EN": "Download Proposal (Markdown)", "BS": "Preuzmi Ponudu (Markdown)"},
    
    # Content strings
    "dev_of": {"EN": "Development of a", "BS": "Razvoj:"},
    "core_modules": {"EN": "Core modules:", "BS": "Osnovni moduli:"},
    "tech_stack": {"EN": "Suggested Technology Stack:", "BS": "Predložene Tehnologije:"},
    "est_weeks": {"EN": "Estimated {start} to {end} weeks", "BS": "Procijenjeno {start} do {end} sedmica"},
    "selling_points": {
        "EN": "HAJ CODE d.o.o. specializes in delivering high-quality, scalable digital solutions. Our agile development process ensures transparency, rapid iteration, and alignment with your business goals. We pride ourselves on technical excellence and a client-centric approach, turning complex requirements into robust applications.",
        "BS": "HAJ CODE d.o.o. je specijalizovan za isporuku visokokvalitetnih, skalabilnih digitalnih rješenja. Naš agilni proces razvoja osigurava transparentnost, brzu iteraciju i usklađenost s vašim poslovnim ciljevima. Ponosimo se tehničkom izvrsnošću i pristupom usmjerenim na klijenta, pretvarajući kompleksne zahtjeve u robusne aplikacije."
    },
    
    # Markdown specifics
    "md_proposal": {"EN": "Project Proposal", "BS": "Prijedlog Projekta"},
    "md_prep_for": {"EN": "Prepared for", "BS": "Pripremljeno za"},
    "md_prep_by": {"EN": "Prepared by", "BS": "Pripremio"},
    "md_overview": {"EN": "1. Project Overview", "BS": "1. Pregled Projekta"},
    "md_thank_you": {
        "EN": "Thank you for considering HAJ CODE d.o.o. for your upcoming {project_type}. Based on our preliminary understanding, this proposal outlines the initial scope, timeline, and estimated investment.",
        "BS": "Hvala Vam što razmatrate HAJ CODE d.o.o. za Vaš nadolazeći projekt ({project_type}). Na osnovu našeg preliminarnog razumijevanja, ova ponuda opisuje početni obim, vremenski okvir i procijenjenu investiciju."
    },
    "md_scope": {"EN": "2. Proposed Project Scope & Tech Stack", "BS": "2. Predloženi Obim Projekta i Tehnologije"},
    "md_time": {"EN": "3. Estimated Time & Cost", "BS": "3. Procijenjeno Vrijeme i Trošak"},
    "md_portfolio": {"EN": "4. Relevant HAJ CODE Portfolio Examples", "BS": "4. Relevantni Primjeri HAJ CODE Portfolija"},
    "md_why": {"EN": "5. Why Choose HAJ CODE d.o.o.?", "BS": "5. Zašto Odabrati HAJ CODE d.o.o.?"}
}

project_types = {
    "Web Application": {"EN": "Web Application", "BS": "Web Aplikacija"},
    "Mobile App (iOS/Android)": {"EN": "Mobile App (iOS/Android)", "BS": "Mobilna Aplikacija (iOS/Android)"},
    "E-commerce Website": {"EN": "E-commerce Website", "BS": "E-commerce Web Stranica"},
    "Custom Software": {"EN": "Custom Software", "BS": "Prilagođeni Softver"},
    "UI/UX Design": {"EN": "UI/UX Design", "BS": "UI/UX Dizajn"},
    "IT Consulting": {"EN": "IT Consulting", "BS": "IT Konsalting"}
}

features_list = {
    "User Authentication": {"EN": "User Authentication", "BS": "Autentifikacija Korisnika"},
    "Payment Gateway Integration": {"EN": "Payment Gateway Integration", "BS": "Integracija Sistema Plaćanja"},
    "Admin Panel": {"EN": "Admin Panel", "BS": "Admin Panel"},
    "API Integration": {"EN": "API Integration", "BS": "API Integracija"},
    "Real-time Chat": {"EN": "Real-time Chat", "BS": "Razgovor u Stvarnom Vremenu"},
    "Location Services": {"EN": "Location Services", "BS": "Usluge Lokacije"},
    "Data Analytics Dashboard": {"EN": "Data Analytics Dashboard", "BS": "Kontrolna Tabla za Analitiku Podataka"},
    "Content Management System (CMS)": {"EN": "Content Management System (CMS)", "BS": "Sistem za Upravljanje Sadržajem (CMS)"},
    "Push Notifications": {"EN": "Push Notifications", "BS": "Push Notifikacije"},
    "Reporting": {"EN": "Reporting", "BS": "Izvještavanje"},
    "Third-Party Integrations": {"EN": "Third-Party Integrations", "BS": "Integracije Trećih Strana"}
}

portfolio_db = {
    "E-commerce Platform X": {
        "EN": "B2C e-commerce platform with custom inventory and payment integrations.",
        "BS": "B2C e-commerce platforma sa prilagođenim sistemom zaliha i integracijama plaćanja."
    },
    "Mobile Event App Y": {
        "EN": "iOS/Android app for real-time event schedules, ticketing, and push notifications.",
        "BS": "iOS/Android aplikacija za rasporede događaja u stvarnom vremenu, prodaju karata i push notifikacije."
    },
    "Logistics Dashboard Z": {
        "EN": "Web application for tracking shipments and managing delivery routes.",
        "BS": "Web aplikacija za praćenje pošiljki i upravljanje rutama isporuke."
    },
    "Healthcare CRM": {
        "EN": "Secure web-based CRM for patient management and appointment scheduling.",
        "BS": "Sigurni web CRM za upravljanje pacijentima i zakazivanje termina."
    }
}

def mock_llm_response(project_data, lang="EN"):
    client_name = project_data.get("client_name", "Valued Client")
    project_title = project_data.get("project_title", "Custom Project")
    project_type = project_data.get("project_type", "Web Application")
    features = project_data.get("features", [])
    timeline = project_data.get("timeline", 12)
    budget = project_data.get("budget", (20000, 50000))
    
    # Generate Scope based on inputs
    tech_stack = "Python, Django, PostgreSQL, React"
    if "Mobile" in project_type:
        tech_stack = "React Native, Node.js, MongoDB"
    elif "E-commerce" in project_type:
        tech_stack = "Shopify/WooCommerce or Custom React/Node.js, Stripe"
    elif "UI/UX" in project_type:
        tech_stack = "Figma, Adobe Creative Suite"
    
    project_type_translated = project_types.get(project_type, {lang: project_type})[lang]
    scope_points = [f"{t['dev_of'][lang]} {project_type_translated}."]
    if features:
        translated_features = [features_list[f][lang] for f in features]
        scope_points.append(f"{t['core_modules'][lang]} {', '.join(translated_features)}.")
    scope_points.append(f"{t['tech_stack'][lang]} {tech_stack}.")
    
    scope = "\n".join([f"- {point}" for point in scope_points])
    
    # Generate Time and Cost based on inputs
    min_budget, max_budget = budget
    est_weeks = t["est_weeks"][lang].format(start=timeline, end=timeline+4)
    time_cost = f"{est_weeks}, €{min_budget:,} - €{max_budget:,}"
    
    # Generate Relevant Projects
    relevant_projects = {}
    if "E-commerce" in project_type or "Payment Gateway Integration" in features:
        relevant_projects["E-commerce Platform X"] = portfolio_db["E-commerce Platform X"][lang]
    if "Mobile" in project_type or "Push Notifications" in features:
        relevant_projects["Mobile Event App Y"] = portfolio_db["Mobile Event App Y"][lang]
    if "Admin Panel" in features or "Data Analytics Dashboard" in features:
        relevant_projects["Logistics Dashboard Z"] = portfolio_db["Logistics Dashboard Z"][lang]
    
    # Default if no specific match
    if not relevant_projects: 
        relevant_projects["Healthcare CRM"] = portfolio_db["Healthcare CRM"][lang]
        relevant_projects["Logistics Dashboard Z"] = portfolio_db["Logistics Dashboard Z"][lang]
        
    # Generate Selling Points Text
    selling_points_text = t["selling_points"][lang]
    
    # Generate Markdown Proposal Content
    relevant_projects_md = ""
    for name, desc in relevant_projects.items():
        relevant_projects_md += f"*   **{name}:** {desc}\n"
        
    thank_you_text = t["md_thank_you"][lang].format(project_type=project_type_translated.lower())
        
    markdown_proposal_content = f"""# {t['md_proposal'][lang]}: {project_title}
**{t['md_prep_for'][lang]}:** {client_name}
**{t['md_prep_by'][lang]}:** HAJ CODE d.o.o.

## {t['md_overview'][lang]}
{thank_you_text}

## {t['md_scope'][lang]}
{scope}

## {t['md_time'][lang]}
**{time_cost}**
{t['preliminary_desc'][lang]}

## {t['md_portfolio'][lang]}
{relevant_projects_md}

## {t['md_why'][lang]}
{selling_points_text}
"""

    return {
        "scope": scope,
        "time_cost": time_cost,
        "relevant_projects": relevant_projects,
        "selling_points_text": selling_points_text,
        "markdown_proposal_content": markdown_proposal_content
    }

# --- UI Implementation ---

# Language Selector
lang = st.radio("Language / Jezik", ["EN", "BS"], horizontal=True)

st.title(t["title"][lang])
st.markdown(t["intro"][lang])

# Input Section
with st.expander(t["client_details"][lang], expanded=True):
    client_name = st.text_input(t["client_name"][lang], key="client_name")
    project_title = st.text_input(t["project_name"][lang], key="project_title")
    
    project_keys = list(project_types.keys())
    project_type = st.selectbox(
        t["project_type"][lang], 
        project_keys, 
        format_func=lambda x: project_types[x][lang],
        key="project_type"
    )
    
    features_keys = list(features_list.keys())
    features = st.multiselect(
        t["features"][lang], 
        features_keys, 
        format_func=lambda x: features_list[x][lang],
        key="features"
    )
    
    description = st.text_area(
        t["desc"][lang], 
        t["desc_placeholder"][lang], 
        height=150, 
        key="description"
    )
    timeline = st.slider(t["timeline"][lang], 2, 52, 12, key="timeline")
    budget = st.slider(
    t["budget"][lang], 
    min_value=100,      # Start from 100
    max_value=15000, 
    value=(20000, 50000), 
    step=100,           # Increment by 100
    key="budget"
)
    
    generate_button = st.button(t["btn_generate"][lang], key="generate_button")

# Output Section
if generate_button:
    if not client_name:
        st.warning(t["err_client"][lang])
    elif not project_title:
        st.warning(t["err_project"][lang])
    else:
        # Gather inputs into a dictionary
        project_data = {
            "client_name": client_name,
            "project_title": project_title,
            "project_type": project_type,
            "features": features,
            "description": description,
            "timeline": timeline,
            "budget": budget
        }
        
        # Simulate LLM call
        with st.spinner(t["analyzing"][lang]):
            response = mock_llm_response(project_data, lang)
            
        # Display Outputs
        st.subheader(f"{t['overview_for'][lang]} {client_name}")
        
        with st.expander(t["scope_title"][lang], expanded=True):
            st.markdown(response["scope"])
            
        with st.expander(t["time_cost_title"][lang], expanded=True):
            st.markdown(f"**{response['time_cost']}**")
            st.caption(t["preliminary_desc"][lang])
            
        with st.expander(t["portfolio_title"][lang], expanded=True):
            for name, desc in response["relevant_projects"].items():
                st.markdown(f"- **{name}:** {desc}")
                
        with st.expander(t["why_title"][lang], expanded=True):
            st.markdown(response["selling_points_text"])
            
        # Download Button
        st.download_button(
            label=t["btn_download"][lang], 
            data=response["markdown_proposal_content"], 
            file_name="HAJ_CODE_Proposal.md" if lang == "EN" else "HAJ_CODE_Ponuda.md",
            mime="text/markdown"
        )
