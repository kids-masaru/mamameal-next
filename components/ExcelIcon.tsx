import React from 'react';

export const ExcelIcon = ({ className }: { className?: string }) => (
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
        <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z" stroke="#22c55e" fill="#dcfce7" />
        <polyline points="14 2 14 8 20 8" stroke="#22c55e" />
        <path d="M8 13h8M8 17h8M8 9h8" stroke="#22c55e" />
        <text x="6" y="20" fontSize="6" fill="#22c55e" fontWeight="bold">XLS</text>
    </svg>
);
