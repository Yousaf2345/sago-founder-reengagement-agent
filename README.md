# Sago – Founder Re-Engagement Agent

This project is a prototype of a workflow-native, agentic AI system designed to help investors re-engage with founders they previously passed on as “too early.”

The agent lives inside Gmail and autonomously tracks founder progress, detects meaningful signals, and executes personalized outreach at the right moment — without requiring the investor to adopt a new tool or workflow.

---

## Problem

Investors frequently meet strong founders who are simply too early. While investors want to follow up later, it is difficult to manually track dozens of founders and know *when* re-engagement is actually meaningful.

As a result:
- Promising opportunities are missed
- Follow-ups are generic or poorly timed
- Investor attention is wasted on noise

---

## Solution

Sago’s Founder Re-Engagement Agent acts as an autonomous assistant that:

1. **Observes** – Tracks founders after an investor marks them as “too early”
2. **Remembers** – Stores investor preferences and prior context
3. **Decides** – Determines when new signals justify re-engagement
4. **Acts** – Drafts and optionally sends personalized outreach inside Gmail

---

## Design Principles Alignment

### Seamless Integration
- Triggered directly from Gmail (label or inline command)
- Outreach happens inside Gmail drafts or sent emails
- No new dashboards or applications required

### Hyper-Personalization
- Maintains long-term memory of:
  - Investor thesis and preferences
  - Reason a founder was previously “too early”
  - Communication style of the investor
- Outreach messages explicitly reference prior context

### True Agency
- The agent autonomously:
  - Monitors external signals
  - Scores signal relevance
  - Decides when to re-engage
  - Generates and executes outreach actions

---

## System Overview

The system is composed of modular components:

- Memory Store – Persistent investor + founder context
- Signal Monitor – Observes external updates (funding, traction, hiring)
- Decision Engine – Determines if signals are meaningful
- Outreach Generator – Drafts personalized messages
- Action Executor – Creates Gmail drafts or sends emails

---

## Status

This repository is a conceptual prototype. External integrations and APIs are mocked to focus on agent logic, decision-making, and system design rather than full implementation.

