from django.shortcuts import render

def home(request):
    """Halaman utama dengan profil pribadi"""
    context = {
        'nama': 'Dimar Renanthera Riyadi',
        'nim': '0110225024',
        'jurusan': 'Teknik Informatika',
        'universitas': 'Sekolah Tinggi Teknologi Terpadu Nurul Fikri',
        'hobi': ['Membaca', 'Bersepeda', 'Coding'],
        'email': 'dimarrenantherariyadi09@gmail.com',
        'telepon': '+62 857-2279-2249',
        'deskripsi': 'Saya adalah seorang mahasiswa Teknik Informatika yang antusias dengan pengembangan web dan teknologi terbaru. Saya senang belajar hal-hal baru dan berkontribusi dalam proyek-proyek yang menantang.',
    }
    return render(request, 'myprofile/home.html', context)

def about(request):
    """Halaman about dengan riwayat pendidikan dan organisasi"""
    pendidikan = [
        {'tahun': '2022-2025', 'institusi': 'SMKS Purnama 1 Depok', 'jurusan': 'Rekayasa Perangkat Lunak'},
        {'tahun': '2025-Sekarang', 'institusi': 'Sekolah Tinggi Teknologi Terpadu Nurul Fikri', 'jurusan': 'Teknik Informatika'},
    ]

    organisasi = [
        {'tahun': '2023-2024', 'nama': 'OSIS SMKS Purnama 1 Depok', 'jabatan': 'Anggota Divisi Acara'},
        {'tahun': '2025-Sekarang', 'nama': 'Himpunan Mahasiswa Teknik Informatika', 'jabatan': 'Anggota Divisi Pengembangan Web'},
    ]

    context = {
        'pendidikan': pendidikan,
        'organisasi': organisasi,
    }
    return render(request, 'myprofile/about.html', context)

def gallery(request):
    """Halaman gallery dengan gambar kegiatan"""
    images = [
        {'title': 'Kampus', 'desc': 'Aktivitas di kampus', 'filename': 'kampus.jpg'},
        {'title': 'Organisasi', 'desc': 'Kegiatan organisasi', 'filename': 'organisasi.jpg'},
        {'title': 'Mentoring', 'desc': 'Mentoring Keagamaan', 'filename': 'mentoring.jpg'},
        {'title': 'Seminar', 'desc': 'Seminar teknologi', 'filename': 'seminar.jpg'},
    ]

    context = {
        'images': images,
    }
    return render(request, 'myprofile/gallery.html', context)
