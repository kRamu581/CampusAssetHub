# 🎓 Campus Asset Hub (CAH)

> **Smarter Asset Management & Lifecycle Optimization for the Modern Campus.**

![ServiceNow](https://img.shields.io/badge/ServiceNow-Platform-2563eb.svg?style=for-the-badge&logo=servicenow)
![Hackathon](https://img.shields.io/badge/LTM_HackNow-2026-53BA00.svg?style=for-the-badge)

## 📖 Overview
Campus bookstores and IT departments face massive issues with manual check-in/check-out of textbooks, lab kits, and laptops. This relies on spreadsheets and paper logs, resulting in long queues, frequent stockouts, and high rates of unreturned assets due to poor tracking. 

**Campus Asset Hub** is a fully automated, self-service SaaS application built natively on ServiceNow. It transforms the asset lifecycle into a seamless digital experience. Students can self-checkout items via mobile QR scanning, manage active assets on a premium Dark-Mode Service Portal, and receive automated AI-driven reminders before items are due.

## ✨ Key Features
* **Premium Dark Mode Portal:** A fully custom Service Portal built with AngularJS, featuring a modern Cyntexa-inspired dark mode UI (`#181818` background with `#53BA00` accents).
* **Mobile QR Checkout:** Students rent/return hardware in <30 seconds via barcode scanning on the Now Mobile app.
* **AI Risk Prediction:** Utilizes ServiceNow Predictive Intelligence to analyze student history and assign a "Predicted Return Risk" (High/Medium/Low) upon checkout.
* **Automated Escalations:** Flow Designer automatically schedules 7-day due dates, calculates late penalties, and restricts users to a single 1-week renewal.
* **Generative AI Reminders:** Automated, highly personalized reminder emails sent to students before deadlines slip.
* **Real-time Command View:** Platform Analytics dashboards give IT admins live visibility into shrinkage, utilization, and overdue hardware.

## 🛠️ Tech Stack
* **ServiceNow App Engine:** Custom Scoped Application & Data Model (`u_asset_allocation`)
* **Service Portal:** Custom UI Widgets (HTML/CSS/Client Scripts)
* **Flow Designer:** Renewal, return, escalation, and notification workflows
* **Hardware Asset Management (HAM):** Core asset lifecycle, serial tracking & depreciation
* **Predictive Intelligence:** Shortage forecasting & delay risk scoring
* **Platform Analytics:** Real-time dashboards and utilization KPIs

## 📈 Projected Business Impact
* **70%+** Reduction in checkout queues
* **40%+** Drop in unreturned assets
* **50%+** Reduction in stockout incidents
* **< 30s** Average checkout time

## 👥 Team Nowscripts
*Built for the LTM HackNow 2026 Hackathon by K.S.R.M. College of Engineering.*
* **Kanam Ramu** - Team Lead & Solution Architect
* **Busetty Balasubramanyam** - App Engine & Catalog Developer
* **Babanbaigari Ummar** - Workflow & AI Developer
* **Avula Sujani** - Mobile, FSM & Analytics Lead

---
*If you are a recruiter reading this, please explore the `/update/` folder to view our custom widget code, CSS styling, and application architecture!*
