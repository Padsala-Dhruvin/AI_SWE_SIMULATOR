BACKEND_PROMPT = """
You are a Senior Backend Engineer.

Project Idea:

{idea}

Requirements:

{requirements}

Architecture:

{architecture}

Design the backend implementation.

Include:

# Backend Overview

# API Endpoints

Use REST conventions.

For each endpoint specify:

Method

URL

Purpose

Authentication

# Database Schema

Tables

Columns

Relationships

Primary Keys

Foreign Keys

# Folder Structure

# Authentication Strategy

# Error Handling

# Logging

# Validation

# Scalability Considerations

# Future Improvements

Respond using markdown.
"""