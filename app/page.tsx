'use client';

import { useState, useRef } from 'react';
import { PdfIcon } from '@/components/PdfIcon';
import { ExcelIcon } from '@/components/ExcelIcon';

export default function Home() {
  const [status, setStatus] = useState<'idle' | 'processing' | 'complete' | 'error'>('idle');
  const [errorMessage, setErrorMessage] = useState('');
  const [downloadUrl, setDownloadUrl] = useState('');
  const [selectedModel, setSelectedModel] = useState('gemini-2.5-flash');
  const fileInputRef = useRef<HTMLInputElement>(null);

  const handleFileChange = async (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (!file) return;
    await processFile(file);
  };

  const processFile = async (file: File) => {
    setStatus('processing');
    setErrorMessage('');

    const formData = new FormData();
    formData.append('file', file);
    formData.append('model', selectedModel);

    try {
      const response = await fetch('/api/process', {
        method: 'POST',
        body: formData,
      });

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.error || 'Processing failed');
      }

      const blob = await response.blob();
      const url = window.URL.createObjectURL(blob);
      setDownloadUrl(url);
      setStatus('complete');
    } catch (err: any) {
      console.error(err);
      setErrorMessage(err.message);
      setStatus('error');
    }
  };

  const handleDragOver = (e: React.DragEvent) => {
    e.preventDefault();
  };

  const handleDrop = async (e: React.DragEvent) => {
    e.preventDefault();
    const file = e.dataTransfer.files?.[0];
    if (file && file.type === 'application/pdf') {
      await processFile(file);
    } else {
      setErrorMessage('Please upload a PDF file.');
    }
  };

  return (
    <main className="min-h-screen bg-orange-50 flex flex-col items-center justify-center p-4 font-sans">
      <div className="max-w-2xl w-full bg-white rounded-2xl shadow-xl p-8 text-center">
        <div className="flex justify-center mb-6">
          <img src="/icon.jpg" alt="App Icon" className="w-24 h-24 rounded-2xl shadow-md" />
        </div>
        <h1 className="text-3xl font-bold text-gray-800 mb-2">数出表 PDF変換ツール</h1>
        <p className="text-gray-500 mb-8">AI (Gemini) を使用して高精度にデータ抽出</p>

        <div className="mb-6 flex justify-center items-center gap-4">
          <label htmlFor="model-select" className="text-gray-700 font-medium">モデル選択:</label>
          <select
            id="model-select"
            value={selectedModel}
            onChange={(e) => setSelectedModel(e.target.value)}
            className="p-2 border border-gray-300 rounded-md shadow-sm focus:border-orange-500 focus:ring focus:ring-orange-200 focus:ring-opacity-50 bg-white"
            disabled={status === 'processing'}
          >
            <option value="gemini-2.0-flash">gemini-2.0-flash</option>
            <option value="gemini-2.5-flash-lite">gemini-2.5-flash-lite</option>
            <option value="gemini-2.5-flash">gemini-2.5-flash (推奨)</option>
            <option value="gemini-2.5-pro">gemini-2.5-pro</option>
            <option value="gemini-3-pro">gemini-3-pro</option>
          </select>
        </div>

        {status === 'idle' || status === 'error' ? (
          <div
            className="border-4 border-dashed border-orange-200 rounded-xl p-10 cursor-pointer hover:bg-orange-50 transition-colors"
            onDragOver={handleDragOver}
            onDrop={handleDrop}
            onClick={() => fileInputRef.current?.click()}
          >
            <input
              type="file"
              ref={fileInputRef}
              className="hidden"
              accept="application/pdf"
              onChange={handleFileChange}
            />
            <div className="flex flex-col items-center">
              <PdfIcon className="w-24 h-24 mb-4 text-orange-500" />
              <p className="text-lg text-gray-600 font-medium">PDFファイルをここにドロップ</p>
              <p className="text-sm text-gray-400 mt-2">またはクリックして選択</p>
            </div>
          </div>
        ) : null}

        {status === 'processing' && (
          <div className="py-12">
            <div className="animate-spin rounded-full h-16 w-16 border-b-2 border-orange-500 mx-auto mb-4"></div>
            <p className="text-lg text-gray-700">AIが解析中... (Gemini)</p>
            <p className="text-sm text-gray-400">これには数秒かかる場合があります</p>
          </div>
        )}

        {status === 'complete' && (
          <div className="py-8 bg-green-50 rounded-xl border border-green-100">
            <div className="flex flex-col items-center">
              <ExcelIcon className="w-24 h-24 mb-4 text-green-600" />
              <h2 className="text-2xl font-bold text-green-700 mb-2">変換完了！</h2>
              <p className="text-gray-600 mb-6">Excelファイルが作成されました</p>

              <a
                href={downloadUrl}
                download="results.zip"
                className="bg-green-600 hover:bg-green-700 text-white font-bold py-3 px-8 rounded-full shadow-lg transition-transform transform hover:scale-105 flex items-center gap-2"
              >
                <svg className="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"></path></svg>
                ダウンロード (ZIP)
              </a>

              <button
                onClick={() => setStatus('idle')}
                className="mt-6 text-gray-500 hover:text-gray-700 underline text-sm"
              >
                別のファイルを変換する
              </button>
            </div>
          </div>
        )}

        {status === 'error' && (
          <div className="mt-6 p-4 bg-red-50 text-red-700 rounded-lg border border-red-200">
            <p className="font-bold">エラーが発生しました</p>
            <p>{errorMessage}</p>
          </div>
        )}
      </div>

      <footer className="mt-12 text-gray-400 text-sm">
        Powered by Vercel & Google Gemini
      </footer>
    </main>
  );
}
