#
# TODO:
# - fix descriptions and summaries to reflect that it isn't rsync but rsyncrypto
#
Summary:	Program for efficient remote updates of files
Summary(es):	Programa para actualizar archivos remotos de forma eficiente
Summary(ko):	네트워크를 통한 파일동기화를 위한 프로그램
Summary(pl):	Program do wydajnego zdalnego uaktualniania plik�w
Summary(pt_BR):	Programa para atualizar arquivos remotos de forma eficiente
Summary(ru):	眺逑怒袴� 켈� 步팍客�肋逑� 臘죈턱卦하 苟卦隆턱�� 팁奸窘
Summary(uk):	眺逑怒皐 켈� 탬탸燉肋逑� 屢컴죈턱逑� 鷗窘謙鑛� 팁奸┹
Summary(zh_CN):	[繫祇]눈渴묏야
Summary(zh_TW):	[놉게]$(B6G?iㆅ(c(B
Name:		rsyncrypto
Version:	0.17
Release:	0.6
License:	GPL v2
Group:		Networking/Utilities
Source0:	http://dl.sourceforge.net/rsyncrypto/%{name}-%{version}.tar.gz
# Source0-md5:	b04df4561d5f9847b647f9c60912d2af
URL:		http://rsync.samba.org/
BuildRequires:	argtable2-devel
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	openssl-devel
Requires:	gzip(rsyncable)
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
rsync is a replacement for rcp that has many more features.

rsync uses the "rsync algorithm" which provides a very fast method for
bringing remote files into sync. It does this by sending just the
differences in the files across the link, without requiring that both
sets of files are present at one of the ends of the link beforehand.

A technical report describing the rsync algorithm is included with
this package.

%description -l es
rsync es un substituto m�s r�pido y flexible para rcp que permite la
sincronizaci�n de archivos o directorios, v�a red, de forma r�pida y
eficiente, entre diferentes m�quinas transfiriendo solamente las
diferencias entre estos directorios de forma compactada. No necesita
que ninguna de las m�quinas tengan una copia de lo que est� en la
otra. Est� disponible en este paquete, una relaci�n t�cnica
describiendo el algoritmo usado por el rsync.

%description -l ko
Rsync는 원격 호스트 파일을 매우 빨리 동기화하는데 신뢰할만한
알고리즘을 사용한다. Rsync는 파일의 전체를 보내는 것 대신에 네트웍을
통해 파일의 다른 부분만을 전송하기 때문에 빠르다. Rsync는 강력한 미러
프로세스 혹은 rcp 커멘드를 통한 더 우수한 대체용으로써 사용된다. rsync
알고리즘을 묘사하는 기술적인 내용은 이 꾸러미에 포함되어 있다.

%description -l pl
Rsync jest zamiennikiem programu rcp z bardziej rozbudowan� sk쿪dni�
polece�. Program ten u퓓wa efektywnego algorytmu "rsync" w czasie
komunikacji i transportu plik�w do systemu zdalnego. Dokumentacja
techniczna nowego algorytmu zosta쿪 r�wnie� do낢czona do pakietu.

%description -l pt_BR
O rsync � um substituto mais r�pido e flex�vel para o rcp permitindo
sincroniza豫o de arquivos ou diret�rios via rede de forma r�pida e
eficiente entre diferentes m�quinas transferindo somente as diferen�as
entre estes diret�rios de forma compactada. Ele n�o precisa que
nenhuma das m�quinas tenha uma c�pia do que est� na outra.

Um relat�rio t�cnico descrevendo o algoritmo usado pelo rsync est�
dispon�vel neste pacote.

%description -l ru
rsync - 卜� 쫏謙� 쬔戇怒� � 핀쫀죙 죈茫텀适燉陸 rcp, 饉璞驅記北�
쬔戇論� � 步팍客�肋藍 饉 鞫卦北炚� � 瑙撞錄죌 膽燉 譚洸碌炚憫촁�
팁奸窘 �俓 個讀卿하� 适 怒蜜�奢謨 皐排适� 檎旽� 斤瑙컨司 冬景蓋
怒蜜�司� 考靈� 炚苽 � 蓋辜瑙幢�碌陸鑛鳩 慄컵. 眺� 卜鳩 遝淪膿턱卦 壙
苟拿죤턍忘�, 師苟� 謳适 皐排适 �考訣 � 膽쫓 蓋筋� 冬하, 師� 텁潼 适
켠朗銶 皐排壙.

%description -l uk
rsync - 쳔 伯�콕� 讀 핑良閘防 죈茫텀适燉陸 rcp, 麒� 憫쩨拍텡邏 伯�켄�
讀 탬탸燉肋� 饉 屢켑郡턱括 켓 瑙撞錄┹ 考瑙輦 譚洸碌過憫챈� 팁奸┹ 司
個讀卿푠� 适 娘剝�� 皐排适� 焙騎鳩 斤瑙컨誹 俓北 屢켐┧卦戇탱 稽� 炚苽
� 蓋辜瑙遝陸卦鼓 慄칡. 眺� 쵤鳩� 博綾┦ 壙 苟窘'拿蓋凜, 粉� 謳适
皐排适 皐訣 � 膽쩨 蓋揆� 冬하, 粉 � 适 ┧魃� 皐排過.

%prep
%setup -q

%build
cp -f /usr/share/automake/config.sub .
%{__autoheader}
%{__autoconf}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
