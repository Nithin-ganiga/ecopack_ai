from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import joblib
import numpy as np
import pandas as pd
import os

#initial fast api set up

app = FastAPI(
    title       = 'EcoPackAI API',
    description = 'AI-Powered Sustainable Packaging Recommendation System',
    version     = '1.0.0'
)

