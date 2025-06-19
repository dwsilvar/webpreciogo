# This file defines API dependencies, such as authentication.

from fastapi import Header, HTTPException, Depends, status
from typing import Annotated