# Standard libraries
import os
import requests
import markdown
import telebot
from telebot import types
from datetime import datetime
from pprint import pprint

# Environment and database handling
from dotenv import load_dotenv
import psycopg2

# BeautifulSoup
import bs4

# LangChain and related modules
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, SystemMessagePromptTemplate
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import (
    PyPDFLoader, Docx2txtLoader, UnstructuredPDFLoader, TextLoader,
    WebBaseLoader, UnstructuredMarkdownLoader, UnstructuredWordDocumentLoader
)
from langchain_community.vectorstores import PGVector
from langchain_community.utilities import SQLDatabase

from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain

# Telegram
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes