import React from 'react';

export const PdfIcon = ({ className }: { className?: string }) => (
    <svg
        xmlns="http://www.w3.org/2000/svg"
        viewBox="0 0 24 24"
        fill="none"
        stroke="currentColor"
        strokeWidth="2"
        strokeLinecap="round"
        strokeLinejoin="round"
        className={className}
    >
        <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z" stroke="#ef4444" fill="#fee2e2" />
        <polyline points="14 2 14 8 20 8" stroke="#ef4444" />
        <path d="M10 13l-2-2m0 0l2-2m-2 2h4" stroke="#ef4444" />
        <text x="6" y="20" fontSize="6" fill="#ef4444" fontWeight="bold">PDF</text>
    </svg>
);
