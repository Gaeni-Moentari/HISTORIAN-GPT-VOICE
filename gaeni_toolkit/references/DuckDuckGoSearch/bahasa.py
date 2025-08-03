# Apa itu DuckDuckGo Search Tool di Langchain? 
# DuckDuckGo Search Tool di Langchain adalah integrasi antara Langchain,
# framework untuk membangun aplikasi berbasis Large Language Models (LLMs),
# dengan DuckDuckGo, mesin pencari yang menekankan privasi.

# DuckDuckGo tidak melacak atau menyimpan informasi pribadi pengguna,
# dan hasil pencarian yang diberikan berfokus pada privasi pengguna.
# Alat ini memungkinkan model LLM di Langchain untuk secara dinamis 
# mencari informasi terbaru dari internet tanpa harus bergantung 
# pada data statis yang ada di model.

# Fungsi Utama:

# Melakukan pencarian internet untuk informasi terbaru.
# Menyediakan alternatif bagi developer yang menginginkan hasil pencarian dengan privasi tinggi.
# Dapat digunakan untuk berbagai aplikasi yang membutuhkan informasi real-time atau dinamis,
# seperti chatbot, asisten AI, dan sistem rekomendasi.

# Review Singkat: DuckDuckGo Search Tool di Langchain 
# sangat berguna bagi pengembang yang menginginkan solusi pencarian
# berbasis privasi untuk aplikasi LLM mereka. Kelebihan alat ini adalah:

# Fokus pada privasi: Tidak menyimpan data pribadi pengguna.
# Pencarian real-time: Mendukung pencarian untuk informasi yang selalu up-to-date,
# berbeda dari model AI yang hanya dilatih pada data historis.

# Kesesuaian dengan Langchain: Mudah diintegrasikan dengan aplikasi berbasis 
# Langchain dan memberikan fleksibilitas dalam hal mendapatkan informasi dari web.

# Namun, kekurangannya terletak pada:

# Hasil pencarian mungkin terbatas: 
#         Jika dibandingkan dengan mesin pencari lain seperti Google,
#     hasil dari DuckDuckGo bisa jadi kurang lengkap atau lebih sedikit dalam beberapa kasus.

# Kurang optimal untuk pencarian yang spesifik atau niche: 

#         Hasil pencarian mungkin tidak selalu mengarah ke sumber daya yang paling relevan, 
#     terutama jika topik pencariannya sangat spesifik.


# Penggunaan Sederhana DuckDuckGo Search Tool di Langchain:

# Langkah pertama yang perlu dilakukan adalah menginstal pustaka 
# yang relevan untuk integrasi dengan DuckDuckGo, kemudian kita bisa 
# menambahkan tool ini ke dalam Chain di Langchain. Berikut adalah contoh 

# kode sederhana untuk menggunakannya:

from langchain.tools import DuckDuckGoSearchRun

# Inisialisasi DuckDuckGo Search Tool
search = DuckDuckGoSearchRun()

# Melakukan pencarian
query = "latest AI trends"
results = search.run(query)

# Menampilkan hasil pencarian
for result in results:
    print(result['title'], result['link'])

# Penggunaan tool ini akan sangat membantu terutama untuk 
# mendapatkan informasi terbaru dan menjaga privasi pengguna 
# tanpa terjebak dalam pelacakan iklan atau data pengguna 
# seperti yang dilakukan oleh mesin pencari lain.
